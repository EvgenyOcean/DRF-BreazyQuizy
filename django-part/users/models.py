from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, 
                    BaseUserManager, PermissionsMixin)
from django.utils import timezone


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **other_fields):
        if not email:
            raise ValueError("Email is required!")

        if not username:
            raise ValueError("Username is required!")

        user = self.model(
            email=self.normalize_email(email), 
            username=username,
            **other_fields,
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, username, password=None, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        user = self.create_user(
            email=email, 
            username=username,
            password=password, 
            **other_fields,
        )

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom User Model itself"""
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)
    about = models.TextField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']