from django.contrib import admin
from .models import Booking  # from current directory model file import Booking model


# Register your models here
@admin.register(Booking)
class BookingsAdmin(admin.ModelAdmin):
    list_display = ('user', 'pet_name', 'service_type', 'booking_time')
