from random import choices

from django.core import validators
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Profile(models.Model):
    MIN_AGE_REQUIREMENT = 12
    MAX_PASSWORD_LENGTH = 30
    MAX_NAME_LENGTH = 30
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


class Game(models.Model):
    MAX_TITLE_LENGTH = 30
    MAX_CATEGORY_LENGTH = 15

    ACTION_GAME = "Action"
    ADVENTURE_GAME = "Adventure"
    PUZZLE_GAME = "Puzzle"
    STRATEGY_GAME = "Strategy"
    SPORTS_GAME = "Sports"
    BOARD_GAME = "Board/Card Game"
    OTHER_GAMES = "Other"

    CATEGORIES = (
        (ACTION_GAME, ACTION_GAME),
        (ADVENTURE_GAME, ADVENTURE_GAME),
        (PUZZLE_GAME, PUZZLE_GAME),
        (STRATEGY_GAME, STRATEGY_GAME),
        (SPORTS_GAME, SPORTS_GAME),
        (BOARD_GAME, BOARD_GAME),
        (OTHER_GAMES, OTHER_GAMES)
    )

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        unique=True,
        null=False,
        blank=False,

    )

    category = models.CharField(
        max_length=MAX_CATEGORY_LENGTH,
        null=False,
        blank=False,
        choices=CATEGORIES
    )

    rating = models.FloatField(
        null=False,
        blank=False,
        validators=(
            MinValueValidator(0.1),
            MaxValueValidator(5.0),
        )
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(1),
        )
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('pk',)