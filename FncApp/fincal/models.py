from django.db import models



# Create your models here.

class Monedas(models.Model):
    moneda = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=255)
    precio = models.FloatField(blank=True, null=True)