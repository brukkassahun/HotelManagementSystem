from django.db import models

class Booking(models.Model):
  bookingNumber = models.CharField(max_length=255)
  name = models.CharField(max_length=255)
  guest = models.CharField(max_length=255)
  roomNumber = models.BigIntegerField()
  extra = models.CharField(max_length=255)
  checkIn = models.DateField()
  checkOut = models.DateField()
  total  = models.FloatField()