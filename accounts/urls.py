from django.urls import path

from accounts import views

"""
URL patterns para o app de contas.

Este módulo define o namespace `account` e mapeia a URL para a view
`InscreverSe`, que lida com a inscrição de novos usuários.

Padrões de URL:
    inscrever/ (views.InscreverSe): Mapeia a URL 'inscrever/' para 
    a view de inscrição.
"""

app_name = 'account'

urlpatterns = [
    path('inscrever/', views.InscreverSe.as_view(), name='InscreverSe'),
    
]