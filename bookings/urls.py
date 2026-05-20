from django.urls import path
from .views import book_service,accepted_bookings,rejected_bookings,completed_bookings,complete_booking,pending_bookings,accept_booking,reject_booking,my_pending_bookings,my_accepted_bookings,my_completed_bookings,my_rejected_bookings

urlpatterns = [
    path('book/<int:service_id>/', book_service, name='book_service'),
    path('my-pending/', my_pending_bookings, name='my_pending'),
    path('my-accepted/', my_accepted_bookings, name='my_accepted'),
    path('my-rejected/', my_rejected_bookings, name='my_rejected'),
    path('my-completed/', my_completed_bookings, name='my_completed'),



    path('pending/', pending_bookings, name='pending_bookings'),
    path('accepted/', accepted_bookings, name='accepted_bookings'),
    path('rejected/', rejected_bookings, name='rejected_bookings'),
    path('completed/', completed_bookings, name='completed_bookings'),



    path('accept/<int:booking_id>/', accept_booking, name='accept_booking'),
    path('reject/<int:booking_id>/', reject_booking, name='reject_booking'),
    path('complete/<int:booking_id>/', complete_booking, name='complete_booking'),
]