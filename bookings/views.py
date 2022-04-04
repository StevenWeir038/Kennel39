from django.shortcuts import render
from .models import Booking
from .forms import BookingForm


def create_booking(request):
    """
    Create booking
    """
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'bookings/create_booking.html', context)


def view_booking(request):
    """
    View booking
    """
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'bookings/view_booking.html', context)
