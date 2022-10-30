from django.core.exceptions import ValidationError


def min_chars_validator(value):
    min_char_length = 2
    if len(value) < min_char_length:
        raise ValidationError("The username must be a minimum of 2 chars")


def validate_year(value):
    min_year = 1979
    max_year = 2050
    if not min_year < value < max_year:
        raise ValidationError("Year must be between 1980 and 2049")
