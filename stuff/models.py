from django.db import models

class Stuff(models.Model):
    stufId=models.TextField()
    firstName=models.TextField()
    lastName=models.TextField()
    email=models.TextField()
    title=models.TextField()
