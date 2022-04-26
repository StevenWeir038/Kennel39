import datetime
from django.db import models
from django.contrib.auth.models import User
from services.models import Service


class Booking(models.Model):
    """
    Booking model
    """

    class AppointmentTime(datetime.time, models.Choices):
        """
        Subclass appointment times for start_time field
        """
        AM_0800 = 8, 0, 0, '08:00'
        AM_0900 = 9, 0, 0, '09:00'
        AM_1000 = 10, 0, 0, '10:00'
        AM_1100 = 11, 0, 0, '11:00'
        PM_1200 = 12, 0, 0, '12:00'
        PM_1300 = 13, 0, 0, '13:00'
        PM_1400 = 14, 0, 0, '14:00'
        PM_1500 = 15, 0, 0, '15:00'
        PM_1600 = 16, 0, 0, '16:00'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=15, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    start_time = models.TimeField(
        choices=AppointmentTime.choices, null=False,
        blank=False, default=AppointmentTime.AM_0800)
    service_type = models.ForeignKey(Service, on_delete=models.CASCADE)

    class Meta:
        """Order bookings by time
        """
        ordering = ['date', 'start_time']

    def __str__(self):
        return str(self.user)
