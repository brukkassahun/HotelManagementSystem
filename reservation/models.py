from django.db import models
from django.utils import timezone

class Reservation(models.Model):
  bookingNumber = models.CharField(max_length=255,default=timezone.now())
  checkIn = models.DateField()
  checkOut = models.DateField()
  firstName = models.CharField(max_length=255)
  middelName = models.CharField(max_length=255)
  lastName = models.CharField(max_length=255)
  contactNumber = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  idCardType = models.CharField(max_length=255)
  idCardNumber = models.CharField(max_length=255)
  roomType = models.CharField(max_length=255)
  roomNumber = models.CharField(max_length=255)
  paymentStatus = models.CharField(max_length=255)
  totalRoomPrice  = models.FloatField(default=0)
  subTotal  = models.FloatField(default=0)
  totalExtraServicePrice  = models.FloatField(default=0)
  isCheckedIn  = models.CharField(max_length=255,default='false')
  isCheckedOut  = models.CharField(max_length=255,default='false')
  extraServices  = models.CharField(max_length=255,default='false')