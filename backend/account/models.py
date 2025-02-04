from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(
        self,
        email, 
        username,
        password,
        **extra_fields
        ):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        if not username:
            raise ValueError(_("The username must be set"))
        user = self.model(
            username=username,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user
    def create_superuser(
        self,
        email, 
        password,
        username,
        **extra_fields
        ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        if not email:
            raise ValueError(_("The Email must be set"))
        if not username:
            raise ValueError(_("The username must be set"))
        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                _("Superuser must have is_staff=True.")
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                _("Superuser must have is_superuser=True.")
            )
        return self.create_user(
            email, 
            username,
            password, 
            **extra_fields
        )


class CustomUser(AbstractUser):
    username = models.CharField(_('username'), max_length=256, unique=True)
    email = models.EmailField(_("email address"), unique=True)
    # Set up the email field as the unique identifier for users.
    # This has nothing to do with the username
    # that we nullified above.
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        'username',
    ]
    objects = CustomUserManager()
    def __str__(self):
        return self.email