from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Booking
from .forms import BookingForm


def view_booking(request):
    """
    View booking
    """
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    return render(request, 'bookings/view_booking.html', context)


@login_required()
def create_booking(request):
    """
    Create booking
    """
    user = get_object_or_404(User, username=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.instance.user = user
            form.save()
            return redirect('view_booking')
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'bookings/create_booking.html', context)


@login_required()
def edit_booking(request, booking_id):
    """
    Edit booking
    """
    user = get_object_or_404(User, username=request.user)
    booking = get_object_or_404(Booking, id=booking_id)
    if booking.user != user:
        return redirect('view_booking')
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('view_booking')
    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'bookings/edit_booking.html', context)


def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('view_booking')
