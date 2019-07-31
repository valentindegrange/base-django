from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

from django.db import models

from .managers import EmailUserManager


class EmailUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    date_joined = models.DateTimeField(
        auto_now_add=True
    )
    is_active = models.BooleanField(
        default=True
    )
    is_staff = models.BooleanField(
        default=False,
    )

    objects = EmailUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
