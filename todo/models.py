from django.db import models

class Tarea(models.Model):
    tarea=models.CharField(max_length=100)
    def __str__(self):
        return self.tarea

class Nota(models.Model):
    descripcion = models.CharField(max_length=120)

    def __str__(self):
        return self.descripcion

# Create your models here.