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
    time = models.DateTimeField()
    humidity1 = models.IntegerField()
    humidity2 = models.IntegerField()
    humidity3 = models.IntegerField()
    temperature1 = models.IntegerField()
    temperature2 = models.IntegerField()
    temperature3 = models.IntegerField()
    leafWettnes = models.IntegerField()
    battery = models.IntegerField()