from django.urls import path
from cleaning.views import (
    Cleaner
)

urlpatterns = [
    path('', Cleaner.as_view(), name='Cleaner'),
]