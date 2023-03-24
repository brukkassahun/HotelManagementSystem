from django.urls import path
from reservation.views import (
    MyView
)

urlpatterns = [
    path('', MyView.as_view(), name='index'),
]