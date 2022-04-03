from django.urls import path
from . import views


urlpatterns = [
    path('', views.create_booking, name='create_booking'),
    path('view-booking', views.view_booking, name='view_booking'),
]
