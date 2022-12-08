from django.db import models

# Create your models here.
class Cliente(models.Model):
    Rut=models.CharField(max_length=50)
    Nombre=models.CharField(max_length=50)
    Apellido=models.CharField(max_length=50)
    Sector=models.CharField(max_length=50)
    Estado=models.CharField(max_length=50)

