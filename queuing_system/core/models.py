from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group, Permission
from django.db import models
from django.utils import timezone
from .choices import c_prioridade
    
class AbrirSolicitacao(models.Model):
    nome_solicitante = models.CharField(blank=True, null=True, max_length=80, verbose_name="Nome do solicitante ")
    prioridade = models.CharField(max_length=20, default='Baixa', verbose_name="Prioridade", choices=c_prioridade)
    info = models.CharField(max_length=400, verbose_name="Informações")
    data_solici = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.nome_solicitante}, {self.info}, {self.data_solici}"
    
