from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Booking
from .forms import BookingForm
from datetime import datetime

num_staff = 2

def view_booking(request):
    """
    View booking
    """
    today_date = datetime.now()
    bookings = Booking.objects.filter(date__gte=today_date)
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
            req_date = form.cleaned_data['date']
            req_time = form.cleaned_data['start_time']
            num_same_bookings = Booking.objects.filter(date=req_date, start_time=req_time).count()
            if num_same_bookings > num_staff:
                return redirect('view_booking')
                messages.add_message(request, messages.error(request, message), "No appointment available for this time")
            else:
                form.instance.user = user
                form.save()
                return redirect('view_booking')
                messages.add_message(request, messages.info, "Appointment confirmed")
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
            # will need same logic here as in create booking to prevent booking clashes.
            form.save()
            return redirect('view_booking')
    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'bookings/edit_booking.html', context)


@login_required()
def cancel_booking(request, booking_id):
    """
    Cancel booking
    """
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('view_booking')
