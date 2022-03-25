from django.contrib import admin
from .models import Booking  # from current directory model file import Booking model

# Register your models here
admin.site.register(Booking)
