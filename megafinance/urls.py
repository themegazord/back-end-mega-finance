from django.urls import path

from megafinance import api

from .api import *

urlpatterns = [
    path('megafinance/clientes/api/', api.ListagemClientes.as_view()),
    path('megafinance/detalhe-cliente/api/<int:pk>/', api.DetalhesCliente.as_view())
]

