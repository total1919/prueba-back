from django.db import models
from django.core.validators import MinValueValidator
from .choices import SALUD 
class Habitat(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_ingreso = models.DateField(null=True, blank=True)
    duracion_estancia = models.IntegerField(validators=[MinValueValidator(0)])
    animal = models.ForeignKey(
        'Animal',  
        on_delete=models.CASCADE,
        related_name='habitats' 
    )

    def __str__(self):
        return self.nombre


class Animal(models.Model):
    nombre_animal = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    peso = models.FloatField(validators=[MinValueValidator(0.0)])  
    fecha_nacimiento = models.DateField()
    salud = models.CharField(max_length=20, choices=SALUD) 
    procedencia = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_animal