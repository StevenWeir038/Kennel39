from django.contrib import admin

from .models import Profile  # from current directory model file import Profile model

# Register your models here
admin.site.register(Profile)
