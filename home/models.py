from django.db import models
from django.contrib.auth.models import User

# Extend allauth user model with an address and contact number

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=False, blank=False)
    address = models.CharField(max_length=50, null=False, blank=False)
