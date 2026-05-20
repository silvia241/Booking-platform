from django.urls import path
from .views import register, user_login,user_logout,buyer_dashboard,seller_dashboard,dashboard_redirect

urlpatterns = [
    path('register/', register),
    path('login/', user_login),
    path('logout/', user_logout),
    path('dashboard/', dashboard_redirect),
    path('buyer/', buyer_dashboard),
    path('seller/', seller_dashboard),
]