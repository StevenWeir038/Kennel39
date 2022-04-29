from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Booking
from .forms import BookingForm
from datetime import datetime


# The number of appointments that can be taken at any given time
num_staff = 1


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
            pet_name = form.cleaned_data['pet_name']
            msg_req_date = req_date.strftime("%A %d, %B, %Y")
            msg_req_time = req_time.strftime("%-I%p")
            num_same_bookings = Booking.objects.filter(
                date=req_date, start_time=req_time).count()
            if num_same_bookings >= num_staff:
                messages.error(
                    request, 'No appointment is available on '
                    f'{msg_req_date} at {msg_req_time}.')
                return redirect('create_booking')
            else:
                form.instance.user = user
                form.save()
                messages.success(
                    request, f'Your appointment for {pet_name} '
                    'has been confirmed.')
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
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            req_date = form.cleaned_data['date']
            req_time = form.cleaned_data['start_time']
            pet_name = form.cleaned_data['pet_name']
            msg_req_date = req_date.strftime("%A, %d %B %Y")
            msg_req_time = req_time.strftime("%-I%p")
            num_same_bookings = Booking.objects.filter(
                date=req_date, start_time=req_time).count()
            if num_same_bookings >= num_staff:
                messages.warning(
                    request, 'No appointment is available or '
                    'this is your booking.')
                return redirect('edit_booking', booking_id)
            else:
                form.save()
                messages.success(request, f'Your appointment for '
                                 f'{pet_name} has been changed.')
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
