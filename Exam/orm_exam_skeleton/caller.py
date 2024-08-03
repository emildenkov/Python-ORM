import os
import django
from django.db.models import Q, Count, F, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Astronaut, Spacecraft, Mission


def get_astronauts(search_string=None):
    if search_string is None:
        return ''

    query = Q(name__icontains=search_string) | Q(phone_number__icontains=search_string)

    astronauts = Astronaut.objects.filter(query).order_by('name')

    if not astronauts.exists():
        return ''

    result = []

    for a in astronauts:
        status = 'Active' if a.is_active else 'Inactive'
        result.append(f'Astronaut: {a.name}, phone number: {a.phone_number}, status: {status}')

    return '\n'.join(result)


def get_top_astronaut():
    astronaut = Astronaut.objects.get_astronauts_by_missions_count().first()

    if not astronaut or astronaut.num_missions == 0:
        return "No data."

    return f"Top Astronaut: {astronaut.name} with {astronaut.num_missions} missions."


def get_top_commander():
    commander = Astronaut.objects.annotate(
        commanded_missions=Count('mission_commander')
    ).order_by(
        '-commanded_missions',
        'phone_number'
    ).first()

    if not commander or commander.commanded_missions == 0:
        return "No data."

    return f"Top Commander: {commander.name} with {commander.commanded_missions} commanded missions."


def get_last_completed_mission():
    mission = Mission.objects.prefetch_related(
        'astronauts',
    ).select_related(
        'spacecraft',
        'commander'
    ).filter(
        status='Completed'
    ).order_by(
        '-launch_date'
    ).first()

    if not mission:
        return "No data."

    commander = mission.commander.name if mission.commander else 'TBA'
    astronauts = ', '.join(mission.astronauts.order_by('name').values_list('name', flat=True))
    spacewalks = sum([s.spacewalks for s in mission.astronauts.all()])
    spacecraft_name = mission.spacecraft.name

    return (f"The last completed mission is: {mission.name}. Commander: {commander}. "
            f"Astronauts: {astronauts}. Spacecraft: {spacecraft_name}. Total spacewalks: {spacewalks}.")


def get_most_used_spacecraft():
    spacecraft = Spacecraft.objects.annotate(
        num_missions=Count('mission_craft', distinct=True),
        num_astonauts=Count('mission_craft__astronauts', distinct=True)
    ).order_by(
        '-num_missions',
        'name'
    ).first()

    if not spacecraft or spacecraft.num_missions == 0:
        return "No data."

    return (f"The most used spacecraft is: {spacecraft.name}, manufactured by {spacecraft.manufacturer}, "
            f"used in {spacecraft.num_missions} missions, astronauts on missions: {spacecraft.num_astonauts}.")


def decrease_spacecrafts_weight():
    spacecrafts = Spacecraft.objects.filter(
        mission_craft__status='Planned',
    ).distinct()
 
    spacecrafts_to_update = spacecrafts.filter(
        weight__gte=200.0
    ).update(
        weight=F('weight') - 200.0
    )

    if spacecrafts_to_update == 0:
        return "No changes in weight."

    avg_weight = Spacecraft.objects.aggregate(avg_weight=Avg('weight'))['avg_weight']

    return (f"The weight of {spacecrafts_to_update} spacecrafts has been decreased. "
            f"The new average weight of all spacecrafts is {avg_weight:.1f}kg")

