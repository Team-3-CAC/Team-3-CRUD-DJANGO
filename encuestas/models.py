from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32) # ejemplo profe: Acabo de craer una tabla que tiene una property que es un var char de 32 caracteres
    dni = models.PositiveIntegerField() # ejemplo profe
    email = models.EmailField(max_length=40, default=None) # Fernando