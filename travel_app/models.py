from django.db import models

class bookings(models.Model):
    user=models.CharField(max_length=64)
    phoneno=models.CharField(max_length=64)
    room=models.IntegerField()
    city=models.CharField(max_length=64,default='puri')
    date=models.DateTimeField()
    price=models.CharField(max_length=64)
