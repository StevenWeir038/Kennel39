from django.shortcuts import render


def create_booking(request):
    """
    Create booking
    """
    return render(request, 'bookings/create_booking.html')


def view_booking(request):
    """
    View booking
    """
    return render(request, 'bookings/view_booking.html')
