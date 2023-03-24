from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginStaff, name='loginStaff'),
    path('logout/', views.logoutStaff, name='logoutStaff'),
]