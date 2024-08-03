import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Author, Book, Review


def find_books_by_genre_and_language(genre, language):
    books = Book.objects.filter(genre=genre, language=language)

    return books


def find_authors_nationalities():
    authors = Author.objects.filter(nationality__isnull=False)

    result = [f"{a.first_name} {a.last_name} is {a.nationality}" for a in authors]

    return "\n".join(result)


def order_books_by_year():
    books = Book.objects.order_by('publication_year', 'title')

    result = [f'{b.publication_year} year: {b.title} by {b.author}' for b in books]

    return "\n".join(result)


def delete_review_by_id(review_id):
    review = Review.objects.get(id=review_id)
    review.delete()

    return f"Review by {review.reviewer_name} was deleted"


def filter_authors_by_nationalities(nationality):
    authors = Author.objects.filter(nationality=nationality).order_by('first_name', 'last_name')
    result = []

    for a in authors:
        if a.biography:
            result.append(a.biography)
        else:
            result.append(f"{a.first_name} {a.last_name}")

    return "\n".join(result)


def filter_authors_by_birth_year(start_year, end_year):
    authors = Author.objects.filter(birth_date__year__range=(start_year, end_year)).order_by('-birth_date')

    result = [f'{a.birth_date}: {a.first_name} {a.last_name}' for a in authors]

    return "\n".join(result)


def change_reviewer_name(reviewer_name, new_name):
    Review.objects.filter(reviewer_name=reviewer_name).update(reviewer_name=new_name)

    return Review.objects.all()
