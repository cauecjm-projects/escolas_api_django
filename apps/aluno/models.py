from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    email = models.EmailField(blank=False, max_length=100, unique=True)
    celular = models.CharField(max_length=14)
    foto = models.ImageField(blank=True)

    def __str__(self):
        return self.nome
