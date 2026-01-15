from django.contrib.auth.models import AbstractUser
from django.db import models

from common.helpers.media_paths import get_media_path_prefix
from common.models import BaseModel

from .choices import UserStatus
from .managers import CustomUserManager


# Create your models here.
class User(AbstractUser, BaseModel):
    username = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=True, db_index=True)
    status = models.CharField(
        max_length=20,
        choices=UserStatus,
        db_index=True,
        default=UserStatus.PENDING,
    )
    avatar = models.ImageField(
        "Avatar",
        upload_to=get_media_path_prefix,
        blank=True,
    )
    ip = models.CharField(max_length=100, blank=True, null=True)
    access_devices = models.TextField(blank=True, null=True)
    joined_date = models.DateTimeField(auto_now_add=True)
    login_otp = models.IntegerField(blank=True, null=True)
    objects = CustomUserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        ordering = ("-date_joined",)

    def __str__(self):
        return f"ID: {self.id}, Username: {self.username}"

    def get_full_name(self):
        return (
            f"{self.first_name} {self.last_name}"
            if self.first_name or self.last_name
            else self.username.capitalize()
        )
