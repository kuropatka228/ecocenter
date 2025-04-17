from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_customer = models.BooleanField(default=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username