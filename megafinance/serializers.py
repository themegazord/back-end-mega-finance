from django.contrib.auth.models import User
from rest_framework import serializers

from .models import *


class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['cod_cliente', 'status_cliente', 'tipo_cliente', 'nome_completo_cliente', 'cpf_cliente', 'cnpj_cliente', 'telefone1_cliente', 'telefone2_cliente', 'rua_endereco_cliente', 'numero_endereco_cliente', 'cep_cliente', 'complemento_endereco_cliente', 'bairro_endereco_cliente', 'email_cliente']
