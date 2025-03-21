from . models import *

def solicData(request):

    dados = AbrirSolicitacao.objects.values('data_solici')
    dados = list(dados)

    filtered = [i['data_solici'] for i in dados]

    return filtered

def solicitacoesFila(request):

    query_dados = AbrirSolicitacao.objects.values('prioridade')

    baixa, media, alta, urgente, imediata = 0, 0, 0, 0, 0

    for i in query_dados:
        if i['prioridade'] == 'Baixa':
            baixa += 1
        elif i['prioridade'] == 'Média':
            media += 1
        elif i['prioridade'] == 'Alta':
            alta += 1
        elif i['prioridade'] == 'Urgente':
            urgente += 1
        elif i['prioridade'] == 'Imediata':
            imediata += 1

    dados = [baixa, media, alta, urgente, imediata]

    # print("Baixa: {}\nMédia: {}\nAlta: {}\nUrgente: {}\nImediata: {}".format(baixa, media, alta, urgente, imediata))

    return dados
