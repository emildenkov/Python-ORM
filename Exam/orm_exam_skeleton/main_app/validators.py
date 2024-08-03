from django.core.exceptions import ValidationError


def only_digits_validator(value):
    for char in value:
        if not char.isdigit():
            raise ValidationError('Only digits allowed')