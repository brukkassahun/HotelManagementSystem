from django.db import models

class FloorType(models.Model):
    floorType=models.CharField(max_length=255)
    price  = models.FloatField()

class Room(models.Model):
    roomNumber=models.IntegerField()
    floorType=models.CharField(max_length=255)
    price  = models.FloatField()
    booking = models.CharField(max_length=255,default='unbooked')
    clean = models.CharField(max_length=255,default='clean')
    
class ExtraServices(models.Model):
    price  = models.FloatField()
    serviceType=models.CharField(max_length=255)
    