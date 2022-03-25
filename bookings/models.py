from django.db import models
from django.contrib.auth.models import User
from services.models import Services


class Booking(models.Model):
    """
    Booking model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=15, null=False, blank=False)
    service_type = models.ForeignKey(Services, on_delete=models.CASCADE)
    booking_time = models.DateTimeField(null=False, blank=False, unique=True)

    class Meta:
        """ Order bookings by date """
        ordering = ['booking_time']

    def __str__(self):
        return str(self.user)
