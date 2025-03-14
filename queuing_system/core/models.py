from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group, Permission
from django.db import models
from django.utils import timezone

class AbrirSolicitacao(models.Model):
    nome_solicitante = models.CharField(blank=True, null=True, max_length=80)
    info = models.CharField(max_length=200)
    data_solici = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nome_solicitante, self.info, self.data_solici
