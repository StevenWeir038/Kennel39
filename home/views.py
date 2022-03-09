from django.shortcuts import render


def index(request):
    """
    Index view
    """
    return render(request, 'home/index.html')
