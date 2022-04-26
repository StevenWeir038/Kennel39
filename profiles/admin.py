from django.contrib import admin
# from current directory model file import Profile model
from .models import Profile

# Register your models here
admin.site.register(Profile)
