from django.contrib import admin
from .models import FloorType,Room

# Register your models here.
admin.site.register(Room)
admin.site.register(FloorType)