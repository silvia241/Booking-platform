from django.urls import path
from .views import service_list,add_service,my_services,edit_service,delete_service

urlpatterns = [
    path('', service_list, name='service_list'),
    path('add/', add_service),
    path('my-services/', my_services, name='my_services'),
    path('edit/<int:service_id>/', edit_service, name='edit_service'),
    path('delete/<int:service_id>/', delete_service, name='delete_service'),
]