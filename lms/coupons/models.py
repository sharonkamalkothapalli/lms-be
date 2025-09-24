from django.db import models
from users.models import User

class Coupons(models.Model):
    STATUS_CHOICE = [
        ("pending", "Pending"),
        ("approved", "Approved"),
        ("denied", "Denied")
    ]

    code = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=16, choices=STATUS_CHOICE, default="pending")

    def __str__(self):
        return f"{self.code} ({self.status})"
