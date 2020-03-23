from django.db import models

# Create your models here.
class Node(models.Model):
    ttnDevId = models.CharField(max_length=32)
    lastSeen = models.DateTimeField(null=True)
    longtitude = models.FloatField()
    lattitude = models.FloatField()

    class Meta:
        ordering = []

class Log(models.Model):
    node = models.ForeignKey('node', on_delete=models.CASCADE, blank=True, null=True)
    ttnTime = models.CharField(max_length=40, null=True)
    localTime = models.DateTimeField(null=True)
    humidity_0 = models.IntegerField()
    humidity_1 = models.IntegerField()
    humidity_2 = models.IntegerField()
    humidity_3 = models.IntegerField()
    temperature_0 = models.IntegerField()
    temperature_1 = models.IntegerField()
    temperature_2 = models.IntegerField()
    temperature_3 = models.IntegerField()
    battery = models.IntegerField()