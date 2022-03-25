from django.contrib import admin
from .models import Services  # from current directory model file import Services model

# Register your models here
admin.site.register(Services)
