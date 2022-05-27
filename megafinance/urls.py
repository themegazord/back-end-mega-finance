from django.urls import path

from megafinance import api

from .api import *

urlpatterns = [
    #Api's Clientes
    path('megafinance/clientes/api/', api.ListagemClientes.as_view()),
    path('megafinance/envia-cliente/api/', api.EnviaCliente.as_view()),
    path('megafinance/detalhe-cliente/api/<int:pk>/', api.DetalhesCliente.as_view()),
    #Api's Fornecedor
    path('megafinance/fornecedores/api/', api.ListagemFornecedor.as_view()),
    path('megafinance/envia-fornecedor/api/', api.EnviaFornecedor.as_view()),
    path('megafinance/detalhe-fornecedor/api/<int:pk>', api.DetalhesFornecedor.as_view()),
    #Api's Titulos
    path('megafinance/titulos/api/', api.ListagemTitulos.as_view()),
    path('megafinance/envia-titulo/api/', api.EnviaTitulo.as_view()),
    path('megafinance/detalhe-titulo/api/<int:pk>/', api.DetalhesTitulos.as_view()),
    #Api's Contas a Pagar
    path('megafinance/contas-a-pagar/api/', api.ListagemContas_A_Pagar.as_view()),
    path('megafinance/envia-contas-a-pagar/api/', api.EnviaContas_A_Pagar.as_view()),
    path('megafinance/detalhe-contas-a-pagar/api/<int:pk>/', api.DetalhesContas_A_Pagar.as_view()),
    #API'S TESTE
    path('megafinance/teste-api/<int:pk>', api.ConsultaClienteTitulo.as_view())
]

