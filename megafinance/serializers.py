from django.contrib.auth.models import User
from rest_framework import serializers

from .models import *


class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['cod_cliente', 'status_cliente', 'tipo_cliente', 'nome_completo_cliente', 'cpf_cliente', 'cnpj_cliente', 'telefone1_cliente', 'telefone2_cliente', 'rua_endereco_cliente', 'numero_endereco_cliente', 'cep_cliente', 'complemento_endereco_cliente', 'bairro_endereco_cliente', 'email_cliente']


class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = ['cod_fornecedor', 'status_fornecedor', 'tipo_fornecedor', 'nome_fornecedor', 'cpf_fornecedor', 'cnpj_fornecedor', 'telefone1_fornecedor', 'telefone2_fornecedor', 'rua_endereco_fornecedor', 'numero_endereco_fornecedor', 'cep_fornecedor', 'complemento_endereco_fornecedor', 'bairro_endereco_fornecedor', 'email_fornecedor']
