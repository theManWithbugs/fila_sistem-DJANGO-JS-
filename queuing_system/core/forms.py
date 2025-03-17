from django import forms
from .models import *

class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = AbrirSolicitacao
        fields = '__all__'
    