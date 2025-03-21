from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import JsonResponse
from .models import *
from .forms import *
from . utils import *

msgSucesso = 'Operação realizada com sucesso!'
msgError = 'Ambos os campos devem ser preenchidos!'
msgIntegridade = 'Você tentou salvar um registro que já existe! Por favor, verifique e tente novamente.'
msgCPF = 'CPF deve conter apenas números!'

def login_view(request):
    template_name = 'account/login.html'
    if request.method == 'GET':
        return render(request, template_name)
    else:
        username = request.POST.get('username')
        password = request.POST.get('senha')

        user = authenticate(username=username, password=password)
    
        if user:
            login(request, user)
            return redirect('home')
        elif password != True:
            messages.error(request, "Senha incorreta!")
            return render(request, template_name)
        else:
            messages.error(request, "Não foi possível realizar o login!")
            return render(request, template_name)
        
def logout_view(request):
    auth_logout(request)
    return redirect('login')

@login_required
def user_view(request):
    template_name = 'account/usuario.html'
    return render(request, template_name)

@login_required
def user_json(request):
    user = request.user
    username = user.username
    email = user.email
    super_usuario = user.is_superuser

    data = {
        'username': username,
        'email': email,
        'is_superuser': super_usuario,
    }
    
    return JsonResponse(data, safe=False)

@login_required
def base_view(request):
    template_name = 'base.html'
    return render(request, template_name)

@login_required
def home_view(request):
    template_name = 'home.html'

    dados = solicData(request)

    return render(request, template_name, {'dados': dados})

def home_json(request):
    dados = solicData(request)

    data = {
        'mensagem': 'nada ainda :(',
        'dados': dados
    }
    return JsonResponse(data)

@login_required
def nova_solicitacao(request):
    template_name = 'include/nova_solicitacao.html'
    
    form = SolicitacaoForm()
    
    if request.method == 'POST':
        form = SolicitacaoForm(request.POST)
        if form.is_valid():
            try:
                form = form.save(commit=False)
                form.nome_solicitante = request.user.username
                form.save()
                messages.success(request, 'Operação realizada com sucesso!')
                return redirect('new_solici')
            except AbrirSolicitacao.DoesNotExist:
                messages.error(request, 'Não foi possível prosseguir!')
        else:
            messages.error(request, 'Formulario invalido!')
    else:
        form = SolicitacaoForm()

    context = {
        'form': form
    }        

    return render(request, template_name, context)

def solicitacoesView(request):
    template_name = 'include/solicitacoes.html'

    query_dados = solicitacoesFila(request)

    baixo = query_dados[0]
    media = query_dados[1]
    alta = query_dados[2]
    urgente = query_dados[3]
    imediata = query_dados[4]

    context = {
        'query_dados': query_dados,
        'baixa': baixo,
        'media': media,
        'alta': alta,
        'urgente': urgente,
        'imediata': imediata,
    }

    return render(request, template_name, context)

    
    

