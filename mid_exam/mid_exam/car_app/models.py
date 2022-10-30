from django.core import validators
from django.db import models

from mid_exam.car_app.validators import min_chars_validator, validate_year


class Profile(models.Model):
    MAX_USER_NAME_LENGTH = 10
    MIN_AGE_REQUIREMENT = 18
    MAX_PASSWORD_LENGTH = 30
    MAX_NAME_LENGTH = 30
    username = models.CharField(
        max_length=MAX_USER_NAME_LENGTH,
        validators=(
            min_chars_validator,
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        validators=(
            validators.MinValueValidator(MIN_AGE_REQUIREMENT),
        ),
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=MAX_PASSWORD_LENGTH,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Car(models.Model):
    MAX_TYPE_CHAR_LENGTH = 10
    MAX_CAR_MODEL_CHAR_LENGTH = 20

    SPORTS_TYPE = "Sports Car"
    PICKUP_TYPE = "Pickup"
    CROSSOVER_TYPE = "Crossover"
    MINIBUS_TYPE = "Minibus"
    OTHER_TYPE = "Other"

    TYPES = (
        (SPORTS_TYPE, SPORTS_TYPE),
        (PICKUP_TYPE, PICKUP_TYPE),
        (CROSSOVER_TYPE, CROSSOVER_TYPE),
        (MINIBUS_TYPE, MINIBUS_TYPE),
        (OTHER_TYPE, OTHER_TYPE),
    )

    car_type = models.CharField(
        max_length=MAX_TYPE_CHAR_LENGTH,
        null=False,
        blank=False,
        choices=TYPES,
    )

    car_model = models.CharField(
        max_length=MAX_CAR_MODEL_CHAR_LENGTH,
        validators=(
            min_chars_validator,
        ),
        null=False,
        blank=False,
    )

    car_year = models.IntegerField(
        validators=(
            validate_year,
        ),
        null=False,
        blank=False,
    )

    car_image = models.URLField(
        null=False,
        blank=False,
    )

    car_price = models.FloatField(
        validators=(
            validators.MinValueValidator(1),
        ),
        null=False,
        blank=False,

    )


