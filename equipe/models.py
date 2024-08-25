from django.db import models

# Create your models here.
class Equipe(models.Model):
    nome = models.CharField(max_length= 200)
    
    fa = {
        ("G", "Graduação"),
        ("M", "Mestrado"),
        ("D", "Doutorado"),
    }
    formacao_academica = models.CharField(max_length=30, choices=fa, default="G")
    
    def __str__(self):
        return self.nome