import os
import django
from django.db.models import F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Pet, Artifact, Location, Car, Task, HotelRoom, Character


def create_pet(name: str, species: str):
    Pet.objects.create(
        name=name,
        species=species
    )

    return f"{name} is a very cute {species}!"


def create_artifact(name: str, origin: str, age: int, description: str, is_magical: bool):
    Artifact.objects.create(
        name=name,
        origin=origin,
        age=age,
        description=description,
        is_magical=is_magical
    )

    return f"The artifact {name} is {age} years old!"


def rename_artifact(artifact: Artifact, new_name: str):
    if artifact.age > 250 and artifact.is_magical:
        artifact.name = new_name
        artifact.save()


def delete_all_artifacts():
    all_artifacts = Artifact.objects.all().delete()


def show_all_locations():
    all_locations = Location.objects.all().order_by('-id')
    result = []

    for location in all_locations:
        result.append(f"{location.name} has a population of {location.population}!")

    return '\n'.join(result)


def new_capital():
    location = Location.objects.first()

    if location:
        location.is_capital = True
        location.save()


def get_capitals():
    locations = Location.objects.filter(is_capital=True)

    return locations.values('name')


def delete_first_location():
    location = Location.objects.first()

    if location:
        location.delete()


def apply_discount():
    cars = Car.objects.all()

    for car in cars:
        discount = sum([int(digit) for digit in str(car.year)])
        discount_percentage = discount / 100

        car.price_with_discount = float(car.price) * (1 - discount_percentage)

    Car.objects.bulk_update(cars, ['price_with_discount'])


def get_recent_cars():
    cars = Car.objects.filter(year__gt=2020)

    return cars.values('model', 'price_with_discount')


def delete_last_car():
    car = Car.objects.last()

    if car:
        car.delete()


def show_unfinished_tasks():
    tasks = Task.objects.filter(is_finished=False)
    result = []

    for task in tasks:
        result.append(f'Task - {task.title} needs to be done until {task.due_date}!')

    return '\n'.join(result)


def complete_odd_tasks():
    tasks = Task.objects.all()

    for task in tasks:
        if task.id % 2 == 1:
            task.is_finished = True

    Task.objects.bulk_update(tasks, ['is_finished'])


def encode_and_replace(text: str, task_title: str):
    tasks = Task.objects.filter(title=task_title)
    message = ''

    for char in text:
        new_char = ord(char) - 3
        message += chr(new_char)

    for task in tasks:
        task.description = message

    Task.objects.bulk_update(tasks, ['description'])


def get_deluxe_rooms():
    rooms = HotelRoom.objects.filter(room_type='Deluxe')

    return '\n'.join(str(room) for room in rooms if room.id % 2 == 0)


def increase_room_capacity():
    rooms = HotelRoom.objects.all().order_by('id')

    previous_capacity = None

    for room in rooms:

        if not room.is_reserved:
            continue

        if previous_capacity is not None:
            room.capacity += previous_capacity
        else:
            room.capacity += room.id

        previous_capacity = room.capacity

    HotelRoom.objects.bulk_update(rooms, ['capacity'])


def reserve_first_room():
    room = HotelRoom.objects.first()
    room.is_reserved = True
    room.save()


def delete_last_room():
    room = HotelRoom.objects.last()

    if not room.is_reserved:
        room.delete()


def update_characters():
    Character.objects.filter(class_name='Mage').update(
        level=F('level') + 3,
        intelligence=F('intelligence') - 7,
    )

    Character.objects.filter(class_name='Warrior').update(
        hit_points=F('hit_points') / 2,
        dexterity=F('dexterity') + 4,
    )

    Character.objects.filter(class_name__in=['Assassin', 'Scout']).update(
        inventory='The inventory is empty',
    )


def fuse_characters(first_character: Character, second_character: Character):
    name = first_character.name + ' ' + second_character.name
    class_name = 'Fusion'
    level = (first_character.level + second_character.level) // 2
    strength = (first_character.strength + second_character.strength) * 1.2
    dexterity = (first_character.dexterity + second_character.dexterity) * 1.4
    intelligence = (first_character.intelligence + second_character.intelligence) * 1.5
    hit_points = (first_character.hit_points + second_character.hit_points)

    if first_character.class_name in ['Mage', 'Scout']:
        inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom"
    else:
        inventory = "Dragon Scale Armor, Excalibur"

    Character.objects.create(
        name=name,
        class_name=class_name,
        level=level,
        strength=strength,
        dexterity=dexterity,
        intelligence=intelligence,
        hit_points=hit_points,
        inventory=inventory,
    )

    first_character.delete()
    second_character.delete()


def grand_dexterity():
    Character.objects.update(dexterity=30)


def grand_intelligence():
    Character.objects.update(intelligence=40)


def grand_strength():
    Character.objects.update(strength=50)


def delete_characters():
    Character.objects.filter(inventory='The inventory is empty').delete()
