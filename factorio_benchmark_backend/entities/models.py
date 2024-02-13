from django.core.exceptions import ValidationError

from django.db import models


def validate_profile_pic(value):
    LIMIT_MB = 1

    limit_bytes = LIMIT_MB * 1024 * 1024
    if len(value) > limit_bytes:
        raise ValidationError(f'The size of the file must be no more than {LIMIT_MB} MB.')


class User(models.Model):
    MAX_USERNAME_LENGTH = 64
    MAX_PASSWORD_HASH_LENGTH = 64
    MAX_DESCRIPTION_LENGTH = 512

    username = models.CharField(
        primary_key=True,
        max_length=MAX_USERNAME_LENGTH,
        validators=[
            MinimumLengthValidator(
                5,
                message='A username must have at least 5 characters.',
            )
        ],
    )
    email = models.EmailField()
    password_hash = models.CharField(max_length=MAX_PASSWORD_HASH_LENGTH)
    profile_pic = models.BinaryField(validators=[validate_profile_pic])
    profile_description = models.CharField(max_length=MAX_DESCRIPTION_LENGTH)


class Scenario(models.Model):
    MAX_TITLE_LENGTH = 64
    MAX_DESCRIPTION_LENGTH = 512

    id = models.PositiveIntegerField(primary_key=True)
    description = models.CharField(max_length=MAX_DESCRIPTION_LENGTH)
    title = models.CharField(max_length=MAX_TITLE_LENGTH)