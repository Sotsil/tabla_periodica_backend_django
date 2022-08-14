from django.db import models

# Create your models here.
class Elementos (models.Model):
    elemento_nombre = models.CharField(max_length=50)
    elemento_simbolo = models.CharField(max_length=50)
    numero_atomico = models.CharField(max_length=50)
    elemento_grupo = models.CharField(max_length=50)

    