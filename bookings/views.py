from django.shortcuts import render


def bookings(request):
    """
    Bookings view
    """
    return render(request, 'bookings/bookings.html')
