from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255, unique=True)
    idade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
