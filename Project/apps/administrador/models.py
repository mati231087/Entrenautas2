from django.db import models

class Administrador(models.Model):
    # Campos del modelo Administrador
    # Ejemplo: nombre, apellido, email, etc.
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # Agrega más campos según tus necesidades

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
from django.db import models

# Create your models here.
