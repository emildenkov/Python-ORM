import os
from datetime import date, timedelta

import django
from django.db.models import Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Author, Book, Artist, Song, Product, Review, Driver, DrivingLicense, Owner, Registration, Car


def show_all_authors_with_their_books():
    authors = Author.objects.all()
    result = []

    for a in authors:
        if a.book_set.count() <= 0:
            continue

        result.append(f'{a.name} has written - {", ".join(b.title for b in a.book_set.all())}!')

    return '\n'.join(result)


def delete_all_authors_without_books():
    Author.objects.filter(book__isnull=True).delete()


def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)


def get_songs_by_artist(artist_name: str):
    artist = Artist.objects.get(name=artist_name)
    return artist.songs.all().order_by('-id')


def remove_song_from_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)


def calculate_average_rating_for_product_by_name(product_name: str):
    product = Product.objects.annotate(avg_rating=Avg('reviews__rating')).get(name=product_name)

    return product.avg_rating


def get_reviews_with_high_ratings(threshold: int):
    reviews = Review.objects.filter(rating__gte=threshold)

    return reviews


def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by('-name')


def delete_products_without_reviews():
    get_products_with_no_reviews().delete()


def calculate_licenses_expiration_dates():
    licenses = DrivingLicense.objects.all().order_by('-license_number')

    return '\n'.join(str(l) for l in licenses)


def get_drivers_with_expired_licenses(due_date: date):
    merit_for_licenses = due_date - timedelta(days=365)

    driver_with_expired_licenses = Driver.objects.filter(license__issue_date__gt=merit_for_licenses)

    return driver_with_expired_licenses


def register_car_by_owner(owner: Owner):
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True).first()

    registration.registration_date = date.today()
    registration.car = car

    car.owner = owner

    car.save()
    registration.save()

    return (f"Successfully registered {car.model} to {owner.name}"
            f" with registration number {registration.registration_number}.")



