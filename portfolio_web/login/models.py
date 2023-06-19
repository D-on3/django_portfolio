from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Add your custom fields here

    class Meta:
        db_table = 'auth_user'
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'user'
        verbose_name_plural = 'users'