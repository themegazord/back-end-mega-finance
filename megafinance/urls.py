from django.urls import path

from megafinance import api

from .api import *

urlpatterns = [
    #Api's Clientes
    path('megafinance/clientes/api/', api.ListagemClientes.as_view()),
    path('megafinance/detalhe-cliente/api/<int:pk>/', api.DetalhesCliente.as_view()),
    #Api's Fornecedor
    path('megafinance/fornecedores/api/', api.ListagemFornecedor.as_view()),
    path('megafinance/detalhe-fornecedor/api/<int:pk>', api.DetalhesFornecedor.as_view()),
    #Api's Titulos
    path('megafinance/titulos/api/', api.ListagemTitulos.as_view()),
    path('megafinance/detalhe-titulo/api/<int:pk>/', api.DetalhesTitulos.as_view()),
]

