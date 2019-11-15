from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from .manager import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True)

    first_name = models.CharField('first name', max_length=30, blank=True)
    middle_name = models.CharField('middle name', max_length=50, blank=True)
    last_name = models.CharField('last name', max_length=50, blank=True)
    # password field supplied by AbstractBaseUser
    # last_login field supplied by AbstractBaseUser

    is_active = models.BooleanField(
        'active',
        default=True,
        help_text=(
            'Designates whether this user should be treated as active.'
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text=(
            'Designates whether the user can log into this admin site.'
        ),
    )

    # is_superuser field provided by PermissionsMixin
    # groups field provided by PermissionsMixin
    # user_permissions field provided by PermissionsMixin

    date_joined = models.DateTimeField(
        'date joined',
        default=timezone.now
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        """
        Return the first name plus the las_name, with a space in between.
        """
        full_name = "{} {}".format(self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return '{} <{}>'.format(self.get_full_name(), self.email)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app 'app_label'?"
        # Simplest possible answer: Yes, always
        return True
