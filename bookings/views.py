from django.shortcuts import render, redirect, get_object_or_404
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


def create_booking(request):
    """
    Create booking
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)  # if there is a post request from the BookingForm
        if form.is_valid():  # check if there are no errors in the form fields
            form.save()  # if no errors then save
            return redirect('view_booking')  # and take the user back to the view_booking page
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'bookings/create_booking.html', context)


def edit_booking(request, booking_id):
    """
    Edit booking
    """
    booking = get_object_or_404(Booking, id=booking_id)  # get instance of the record or retur 404 error if nothing found
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
