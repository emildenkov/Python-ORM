from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from main_app.managers import AstronautManager
from main_app.validators import only_digits_validator
from main_app.choices import StatusChoices


class NameMixin(models.Model):
    name = models.CharField(
        max_length=120,
        validators=[
            MinLengthValidator(2),
        ]
    )

    class Meta:
        abstract = True


class UpdatedAtMixin(models.Model):
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        abstract = True


class LaunchDateMixin(models.Model):
    launch_date = models.DateField()

    class Meta:
        abstract = True


class Astronaut(NameMixin, UpdatedAtMixin):
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            only_digits_validator
        ]
    )
    is_active = models.BooleanField(
        default=True
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )
    spacewalks = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
        ]
    )

    objects = AstronautManager()

    def __str__(self):
        return self.name


class Spacecraft(NameMixin, LaunchDateMixin, UpdatedAtMixin):
    manufacturer = models.CharField(
        max_length=100,
    )
    capacity = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
        ]
    )
    weight = models.FloatField(
        validators=[
            MinValueValidator(0.0),
        ]
    )

    def __str__(self):
        return self.name


class Mission(NameMixin,LaunchDateMixin, UpdatedAtMixin):
    description = models.TextField(
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=9,
        choices=StatusChoices,
        default=StatusChoices.PLANNED
    )
    spacecraft = models.ForeignKey(
        to=Spacecraft,
        on_delete=models.CASCADE,
        related_name='mission_craft'
    )
    astronauts = models.ManyToManyField(
        to=Astronaut,
        related_name='mission_astronauts',
    )
    commander = models.ForeignKey(
        to=Astronaut,
        on_delete=models.SET_NULL,
        null=True,
        related_name='mission_commander',
    )

    def __str__(self):
        return self.status
