from django.urls import path
from booked.views import (
    MyView
)

urlpatterns = [
    path('', MyView.as_view(), name='index'),
]