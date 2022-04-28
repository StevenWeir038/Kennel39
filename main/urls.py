from django.contrib import admin
from django.urls import path, include
from .views import handler404, handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('services/', include('services.urls')),
    path('bookings/', include('bookings.urls')),
]

handler404 = 'main.views.handler404'
handler500 = 'main.views.handler500'
