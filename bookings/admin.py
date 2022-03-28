from django.contrib import admin
from .models import Booking


# Register your models here
@admin.register(Booking)
class BookingsAdmin(admin.ModelAdmin):
    search_fields = ['pet_name']
    list_display = ('user', 'pet_name', 'date', 'start_time', 'service_type')
    list_filter = ('date', 'service_type')
