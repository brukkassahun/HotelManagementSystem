from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.booking, name='book'),
    path('profile/', views.profile, name='profile'),
]