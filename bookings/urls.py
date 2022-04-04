from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_booking, name='view_booking'),
    path('create-booking', views.create_booking, name='create_booking'),
]
