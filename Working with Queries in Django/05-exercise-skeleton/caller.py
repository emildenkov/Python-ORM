import os
from typing import List

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import ArtworkGallery, ChessPlayer, Meal, Dungeon, Workout, Laptop


def show_highest_rated_art():
    artwork = ArtworkGallery.objects.order_by('-rating', 'id').first()

    return f"{artwork.art_name} is the highest-rated art with a {artwork.rating} rating!"


def bulk_create_arts(first_art: ArtworkGallery, second_art: ArtworkGallery):
    arts = [
        first_art,
        second_art
    ]

    ArtworkGallery.objects.bulk_create(arts)


def delete_negative_rated_arts():
    ArtworkGallery.objects.filter(rating__lt=0).delete()


def show_the_most_expensive_laptop():
    laptop = Laptop.objects.order_by('-price', '-id').first()

    return f'{laptop.brand} is the most expensive laptop available for {laptop.price}$!'


def bulk_create_laptops(args: List[Laptop]):
    Laptop.objects.bulk_create(args)


def update_to_512_GB_storage():
    Laptop.objects.filter(brand__in=['Asus', 'Lenovo']).update(storage=512)


def update_to_16_GB_memory():
    Laptop.objects.filter(brand__in=['Apple', 'Dell', 'Acer']).update(memory=16)


def update_operation_systems():
    laptops = Laptop.objects.all()

    for laptop in laptops:
        if laptop.brand == 'Apple':
            laptop.operation_system = 'MacOS'
        elif laptop.brand in ['Dell', 'Acer']:
            laptop.operation_system = 'Linux'
        elif laptop.brand == 'Lenovo':
            laptop.operation_system = 'Chrome OS'
        elif laptop.brand == 'Asus':
            laptop.operation_system = 'Windows'

    Laptop.objects.bulk_update(laptops, ['operation_system'])


def delete_inexpensive_laptops():
    Laptop.objects.filter(price__lt=1200).delete()


def bulk_create_chess_players(args: List[ChessPlayer]):
    ChessPlayer.objects.bulk_create(args)


def delete_chess_players():
    ChessPlayer.objects.filter(title='no title').delete()


def change_chess_games_won():
    ChessPlayer.objects.filter(title="GM").update(games_won=30)


def change_chess_games_lost():
    ChessPlayer.objects.filter(title="no title").update(games_lost=25)


def change_chess_games_drawn():
    ChessPlayer.objects.all().update(games_drawn=10)


def grand_chess_title_GM():
    ChessPlayer.objects.filter(rating__gte=2400).update(title='GM')


def grand_chess_title_IM():
    ChessPlayer.objects.filter(rating__range=(2300, 2399)).update(title='IM')


def grand_chess_title_FM():
    ChessPlayer.objects.filter(rating__range=(2200, 2299)).update(title='FM')


def grand_chess_title_regular_player():
    ChessPlayer.objects.filter(rating__range=(0, 2199)).update(title='regular player')


def set_new_chefs():
    Meal.objects.filter(meal_type='Breakfast').update(chef='Gordon Ramsay')
    Meal.objects.filter(meal_type='Lunch').update(chef='Julia Child')
    Meal.objects.filter(meal_type='Dinner').update(chef='Jamie Oliver')
    Meal.objects.filter(meal_type='Snack').update(chef='Thomas Keller')


def set_new_preparation_times():
    Meal.objects.filter(meal_type='Breakfast').update(preparation_time='10 minutes')
    Meal.objects.filter(meal_type='Lunch').update(preparation_time='12 minutes')
    Meal.objects.filter(meal_type='Dinner').update(preparation_time='15 minutes')
    Meal.objects.filter(meal_type='Snack').update(preparation_time='5 minutes')


def update_low_calorie_meals():
    Meal.objects.filter(meal_type__in=['Breakfast', 'Dinner']).update(calories=400)


def update_high_calorie_meals():
    Meal.objects.filter(meal_type__in=['Lunch', 'Snack']).update(calories=700)


def delete_lunch_and_snack_meals():
    Meal.objects.filter(meal_type__in=['Lunch', 'Snack']).delete()


def show_hard_dungeons():
    dungeons = Dungeon.objects.filter(difficulty='Hard').order_by('-location')

    result = [f'{d.name} is guarded by {d.boss_name} who has {d.boss_health} health points!' for d in dungeons]

    return "\n".join(result)


def bulk_create_dungeons(args: List[Dungeon]):
    Dungeon.objects.bulk_create(args)


def update_dungeon_names():
    Dungeon.objects.filter(difficulty='Easy').update(name='The Erased Thombs')
    Dungeon.objects.filter(difficulty='Medium').update(name='The Coral Labyrinth')
    Dungeon.objects.filter(difficulty='Hard').update(name='The Lost Haunt')


def update_dungeon_bosses_health():
    Dungeon.objects.exclude(difficulty='Easy').update(boss_health=500)


def update_dungeon_recommended_levels():
    Dungeon.objects.filter(difficulty='Easy').update(recommended_level=25)
    Dungeon.objects.filter(difficulty='Medium').update(recommended_level=50)
    Dungeon.objects.filter(difficulty='Hard').update(recommended_level=75)


def update_dungeon_rewards():
    Dungeon.objects.filter(boss_health=500).update(reward='1000 Gold')
    Dungeon.objects.filter(location__startswith='E').update(reward='New dungeon unlocked')
    Dungeon.objects.filter(location__endswith='s').update(reward='Dragonheart Amulet')


def set_new_locations():
    Dungeon.objects.filter(recommended_level=25).update(location='Enchanted Maze')
    Dungeon.objects.filter(recommended_level=50).update(location='Grimstone Mines')
    Dungeon.objects.filter(recommended_level=75).update(location='Shadowed Abyss')


def show_workouts():
    workouts = Workout.objects.filter(workout_type__in=["Calisthenics", "CrossFit"]).order_by('id')

    result = [f'{w.name} from {w.workout_type} type has {w.difficulty} difficulty!' for w in workouts]

    return "\n".join(result)


def get_high_difficulty_cardio_workouts():
    workouts = Workout.objects.filter(workout_type='Cardio').order_by('instructor')

    return workouts


def set_new_instructors():
    Workout.objects.filter(workout_type='Cardio').update(instructor='John Smith')
    Workout.objects.filter(workout_type='Strength').update(instructor='Michael Williams')
    Workout.objects.filter(workout_type='Yoga').update(instructor='Emily Johnson')
    Workout.objects.filter(workout_type='CrossFit').update(instructor='Sarah Davis')
    Workout.objects.filter(workout_type='Calisthenics').update(instructor='Chris Heria')


def set_new_duration_times():
    Workout.objects.filter(instructor='John Smith').update(duration='15 minutes')
    Workout.objects.filter(instructor='Sarah Davis').update(duration='30 minutes')
    Workout.objects.filter(instructor='Chris Heria').update(duration='45 minutes')
    Workout.objects.filter(instructor='Michael Williams').update(duration='1 hour')
    Workout.objects.filter(instructor='Emily Johnson').update(duration='1 hour and 30 minutes')


def delete_workouts():
    Workout.objects.exclude(workout_type__in=["Strength", "Calisthenics"]).delete()
