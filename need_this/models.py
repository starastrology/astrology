from django.db.models import fields
from django.db import models
class Zodiac(models.Model):
    sign = fields.CharField(max_length=15)
    value = fields.IntegerField(primary_key=True)
class Individual(models.Model):
    name = fields.CharField(max_length=50, unique=True)
    wiki = fields.CharField(max_length=100)
    north = fields.BooleanField(default=True)
    zodiac = models.ForeignKey(Zodiac, on_delete=models.CASCADE)