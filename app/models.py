from django.db import models

# Create your models here.
class Carros(models.Model):
    modelo = models.CharField(max_length=150)
    marca = models.CharField(max_length=20)
    ano = models.IntegerField()
    data = models.DateTimeField("data"=now)
    