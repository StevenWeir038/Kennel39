from django.shortcuts import render


def services(request):
    """
    Services view
    """
    return render(request, 'services/services.html')
