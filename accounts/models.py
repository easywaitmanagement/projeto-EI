from django.db import models

class Registo(models.Model):
    nome_completo = models.CharField(max_length=100, unique=True)
    idade = models.PositiveIntegerField()
    sexo = models.CharField(max_length=6, choices=[('M', 'Male'), ('F', 'Female'), ('Outro', 'Other')])
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome_completo

class Users(models.Model):
    registo = models.OneToOneField(Registo, on_delete=models.CASCADE)
    user = models.CharField(max_length=50, unique=True)
    palavra_passe = models.CharField(max_length=50)

    def __str__(self):
        return self.user