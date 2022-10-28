from django.core import validators
from django.db import models

from music_app_django.web.validators import alphanumeric_validator


class Profile(models.Model):
    MIN_NAME_LENGTH = 2
    MAX_NAME_LENGTH = 15

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        null=False,
        blank=False,
        validators=(
            validators.MinLengthValidator(MIN_NAME_LENGTH),
            alphanumeric_validator,
        ),
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=False,
        blank=True,
    )


class Album(models.Model):
    MAX_NAME_LENGTH = 30
    MAX_ARTIST_LENGTH = 30
    MAX_GENRE_LENGTH = 30

    POP_MUSIC = "Pop Music"
    JAZZ_MUSIC = "Jazz Music"
    RNB_MUSIC = "R&B Music"
    ROCK_MUSIC = "Rock Music"
    COUNTRY_MUSIC = "Country Music"
    DANCE_MUSIC = "Dance Music"
    HIP_HOP_MUSIC = "Hip Hop Music"
    OTHER_MUSIC = "Other"

    MUSICS = (
        (POP_MUSIC, POP_MUSIC),
        (JAZZ_MUSIC, JAZZ_MUSIC),
        (RNB_MUSIC, RNB_MUSIC),
        (ROCK_MUSIC, ROCK_MUSIC),
        (COUNTRY_MUSIC, COUNTRY_MUSIC),
        (DANCE_MUSIC, DANCE_MUSIC),
        (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
        (OTHER_MUSIC, OTHER_MUSIC)
    )

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        unique=True,
        null=False,
        blank=False,
    )

    artist = models.CharField(
        max_length=MAX_ARTIST_LENGTH,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=MAX_GENRE_LENGTH,
        null=False,
        blank=False,
        choices=MUSICS
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=(
            validators.MinValueValidator(0.0),
        )
    )

    description = models.TextField(
        null=True,
        blank=True,
    )