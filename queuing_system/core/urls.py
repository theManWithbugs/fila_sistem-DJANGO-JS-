from django.urls import path
from core import views
from django.conf import settings
from core.views import *

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/usuario/', views.user_view, name='usuario'),

    path('base/', views.base_view, name='base'),
    path('home/', views.home_view, name='home'),
    path('home/nova_solicitacao/', views.nova_solicitacao, name='new_solici'),

    # Json response
    path('home/usuario/json_response/', views.user_json, name='user_json'),
]