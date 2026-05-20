
from django.contrib import admin
from django.urls import path,include
from core.views import home

urlpatterns = [
    path('', home),

    path('admin/', admin.site.urls),

    path('services/', include('services.urls')),
    path('booking/', include('bookings.urls')),
    path('accounts/', include('accounts.urls')),

]
