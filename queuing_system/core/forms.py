from django import forms
from .models import *

class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = AbrirSolicitacao
        fields = '__all__'
        exclude = ['nome_solicitante', 'data_solici']
        widgets = {
            'info': forms.Textarea(attrs={
                'class': 'form-control form-control-sm',
                'rows': 4, 
                'placeholder': 'Digite informações aqui...',
            }),
            'prioridade': forms.Select(attrs={
                'class': 'form-select',
                'size': 3,
                'placeholder': 'Selecione a prioridade...',
            }),
        }
    