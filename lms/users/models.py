from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        (1, "user"),
        (2, "approver"),
        (3, "creator")
    )

    role = models.PositiveSmallIntegerField(default=1, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} role=({self.get_role_display()})"