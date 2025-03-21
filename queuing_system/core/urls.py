from django.urls import path
from core import views
from django.conf import settings
from core.views import *

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/usuario/', views.user_view, name='usuario'),
    path('home/usuario/json_response/', views.user_json, name='user_json'),

    path('base/', views.base_view, name='base'),
    path('home/', views.home_view, name='home'),
    path('home/home_json/', views.home_json, name='home_json'),

    path('home/solicitacoes/', views.solicitacoesView, name='solicitacoes'),

    path('home/nova_solicitacao/', views.nova_solicitacao, name='new_solici'),
]