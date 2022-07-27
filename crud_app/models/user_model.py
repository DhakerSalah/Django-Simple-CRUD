from datetime import date
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

GENDER = (
    ('femme', 'Femme'),
    ('homme', 'Homme'),
    ('other', 'Other'),
)

class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, username, password=None, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not username:
            raise ValueError('The given phone must be set')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        """Create and save a SuperUser with the given phone and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class CustomUser(AbstractUser):
    password = models.CharField(_('password'), max_length=128, blank=True)
    phone_number = models.CharField(max_length=200, blank=True, unique=True)
    gender = models.CharField(max_length=5, choices=GENDER, blank=True)
    birth_date = models.DateField(default=date.today, blank=True)
    is_manager = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.phone_number)
