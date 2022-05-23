from tabnanny import verbose
from tkinter import N

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone


# Create your models here.
class Cliente(models.Model):
    STATUS_CLIENTES = [
        ('A', 'Ativo'),
        ('I', 'Inativo')
    ]

    TIPO_CLIENTE_CHOICES = [
        ('F', 'Pessoa Fisica'),
        ('J', 'Pessoa Juridica')
    ]

    cod_cliente = models.SmallAutoField(primary_key=True, unique=True, verbose_name='Código de Cliente')
    status_cliente = models.CharField(max_length=1, choices=STATUS_CLIENTES, default='', verbose_name='Status')
    tipo_cliente = models.CharField(max_length=1, choices=TIPO_CLIENTE_CHOICES, default='', verbose_name='Tipo do Cliente')
    nome_completo_cliente = models.CharField(max_length=155, verbose_name='Nome do Cliente')
    cpf_cliente = models.CharField(max_length=14, unique=True, blank=True, null=True, verbose_name='CPF')
    cnpj_cliente = models.CharField(max_length=18, unique=True, blank=True, null=True, verbose_name='CNPJ')
    telefone1_cliente = models.CharField(max_length=25, blank=True, null=True, verbose_name='Telefone Fixo')
    telefone2_cliente = models.CharField(max_length=25, blank=True, null=True, verbose_name='Telefone Celular')
    rua_endereco_cliente = models.CharField(max_length=155, verbose_name='Endereço')
    numero_endereco_cliente = models.CharField(max_length=10, verbose_name='Número')
    cep_cliente = models.CharField(max_length=9, default='', verbose_name='CEP')
    complemento_endereco_cliente = models.CharField(max_length=155, verbose_name='Complemento', blank=True, null=True)
    bairro_endereco_cliente = models.CharField(max_length=155, verbose_name='Bairro')
    email_cliente = models.EmailField(verbose_name='E-mail', blank=True, null=True)

    def __str__(self):
        return self.nome_completo_cliente



class Fornecedor(models.Model):
    STATUS_FORNECEDORES_CHOICES = [
        ('A', 'Ativo'),
        ('I', 'Inativo')
    ]

    TIPO_FORNECEDOR_CHOICES = [
        ('F', 'Pessoa Fisica'),
        ('J', 'Pessoa Juridica')
    ]

    cod_fornecedor = models.SmallAutoField(primary_key=True, unique=True, verbose_name='Código do Fornecedor')
    status_fornecedor = models.CharField(max_length=1, choices=STATUS_FORNECEDORES_CHOICES, default='', verbose_name='Status do Fornecedor')
    tipo_fornecedor = models.CharField(max_length=1, choices=TIPO_FORNECEDOR_CHOICES, default='', verbose_name='Tipo do Fornecedor')
    nome_fornecedor = models.CharField(max_length=155, verbose_name='Nome do Fornecedor')
    cpf_fornecedor = models.CharField(max_length=14, unique=True, blank=True, null=True, verbose_name='CPF do Fornecedor')
    cnpj_fornecedor = models.CharField(max_length=18, unique=True, blank=True, null=True, verbose_name='CNPJ do Fornecedor')
    telefone1_fornecedor = models.CharField(max_length=25, blank=True, null=True, verbose_name='Telefone Fixo')
    telefone2_fornecedor = models.CharField(max_length=25, blank=True, null=True, verbose_name='Telefone Celular')
    rua_endereco_fornecedor = models.CharField(max_length=155, verbose_name='Endereço do Fornecedor')
    numero_endereco_fornecedor = models.CharField(max_length=10, verbose_name='Numero de Endereço')
    cep_fornecedor = models.CharField(max_length=9, default='', verbose_name='CEP')
    complemento_endereco_fornecedor = models.CharField(max_length=155,blank=True, null=True, verbose_name='Complemento')
    bairro_endereco_fornecedor = models.CharField(max_length=155, verbose_name='Bairro')
    email_fornecedor = models.EmailField(verbose_name='Email do Fornecedor', blank=True, null=True)

    def __str__(self):
        return self.nome_fornecedor


class Titulo(models.Model):
    STATUS_TITULO_CHOICES = [
        ('A', 'Aberto'),
        ('F', 'Fechado')
    ]

    PAGAR_RECEBER_CHOICES = [
        ('P', 'Contas a Pagar'),
        ('R', 'Contas a Receber')
    ]
    
    cod_titulo = models.SmallAutoField(primary_key=True, unique=True, verbose_name='Código do Titulo')
    status_titulo = models.CharField(max_length=1, choices=STATUS_TITULO_CHOICES, blank=True, null=True, default='A', verbose_name='Status do Titulo')
    descricao_titulo = models.CharField(max_length=155, verbose_name='Descrição do Titulo')
    pagar_receber_titulo = models.CharField(max_length=1, choices=PAGAR_RECEBER_CHOICES, blank=True, null=True, default='', verbose_name='Pagar ou Receber')
    data_inicio_titulo = models.DateTimeField(default=timezone.now, verbose_name='Data de Inicio do Titulo')
    data_final_titulo = models.DateTimeField(verbose_name='Data final do Titulo')

    def __str__(self):
        return self.descricao_titulo


class Contas_A_Pagar(models.Model):
    cod_contas_a_pagar = models.SmallAutoField(primary_key=True, unique=True, verbose_name='Código Contas a Pagar')
    nome_fornecedor_contas_a_pagar = models.ForeignKey(Fornecedor, on_delete=models.SET_NULL, null=True, blank=True, related_name='nome_fornecedor_contas_a_pagar', verbose_name='Nome fornecedor')
    cod_titulo = models.OneToOneField(Titulo, on_delete=models.CASCADE, verbose_name='Código do Titulo')
    valor_titulo_a_pagar = models.PositiveIntegerField(verbose_name='Valor do Titulo')
    valor_desconto_a_pagar = models.PositiveIntegerField(
        validators=[
                MinValueValidator(0), 
                MaxValueValidator(100)
            ],
            verbose_name='Desconto do Titulo'
        )



class Contas_A_Receber(models.Model):
    cod_contas_a_receber = models.SmallAutoField(primary_key=True, unique=True, verbose_name='Código Contas a Receber')
    nome_clinete_contas_a_pagar = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True, related_name='nome_cliente', verbose_name='Nome do Cliente')
    cod_titulo = models.OneToOneField(Titulo, on_delete=models.CASCADE, verbose_name='Código do Titulo')
    valor_titulo_a_receber = models.PositiveIntegerField(verbose_name='Valor Titulo a Receber')
    desconto_titulo_a_receber = models.PositiveIntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ],
        verbose_name='Desconto Titulo a Receber'
    )



class Grupo_Produtos(models.Model):
    cod_grupo = models.SmallAutoField(primary_key=True, unique=True, verbose_name='Código do Grupo')
    nome_grupo = models.CharField(max_length=50, verbose_name='Nome do Grupo')

    def __str__(self):
        return self.nome_grupo


class SubGrupo_Produtos(models.Model):
    cod_subgrupo = models.SmallAutoField(primary_key=True, unique=True, verbose_name='Código de Subgrupo')
    nome_subgrupo = models.CharField(max_length=50, verbose_name='Nome do Subgrupo')
    def __str__(self):
        return self.nome_subgrupo


class Unidade_Produtos(models.Model):
    cod_unidade = models.SmallAutoField(primary_key=True, unique=True, verbose_name='Código Unidade')
    sigle_unidade = models.CharField(max_length=5, verbose_name='Sigla unidade')
    nome_unidade = models.CharField(max_length=50, verbose_name='Nome da Unidade')
    def __str__(self):
        return self.nome_unidade

class Produtos(models.Model):
    STATUS_PRODUTOS = [
        ('A', 'Ativo'),
        ('I', 'Inativo'),
    ]
    TIPO_PRODUTO = [
        ('M', 'Matéria Prima'),
        ('A', 'Produto Acabado'),
        ('E', 'Embalagem'),
    ]
    cod_produto = models.SmallAutoField(primary_key=True, unique=True, verbose_name='Código do Produto')
    nome_produto = models.CharField(max_length=155, verbose_name='Nome do Produto')
    status_produto = models.CharField(max_length=1, choices=STATUS_PRODUTOS, verbose_name='Status do Produto')
    tipo_produto = models.CharField(max_length=1, choices=TIPO_PRODUTO, verbose_name='Tipo do Produto')
    grupo_produto = models.ForeignKey(Grupo_Produtos, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Grupo')
    subgrupo_produto = models.ForeignKey(SubGrupo_Produtos, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Subgrupo')
    unidade_produto = models.ForeignKey(Unidade_Produtos, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Unidade do Produto')
    valor_produto = models.IntegerField(verbose_name='Valor do Produto')
    custo_produto = models.IntegerField(verbose_name='Custo do Produto')

    def __str__(self):
        return self.nome_produto



class Receitas(models.Model):
    cod_receita = models.SmallAutoField(primary_key=True, unique=True, verbose_name='Código da Receita')
    nome_ficha_producao = models.CharField(max_length=155, verbose_name='Nome da Ficha de Produção')
    produto_acabado_producao = models.ForeignKey(Produtos, on_delete=models.SET_NULL, blank=True, null=True, related_name="cod_produto_acabado", verbose_name='Produto acabado')
    produto_emabalagem_producao = models.ForeignKey(Produtos, on_delete=models.SET_NULL, blank=True, null=True, related_name="cod_produto_emabalagem", verbose_name='Produto embalagem')
    preco_custo_produto_producao = models.ForeignKey(Produtos, on_delete=models.SET_NULL, blank=True, null=True, related_name="custo_produto_producao", verbose_name='Custo da Produção')
    margem_lucro_produto_producao = models.IntegerField(verbose_name='Margem de Lucro')
    def __str__(self):
        return self.nome_ficha_producao


class Produtos_Receitas(models.Model):
    cod_produto_receita = models.SmallAutoField(primary_key=True, unique=True, verbose_name='Código da Lista de Produtos')
    cod_receita = models.OneToOneField(Receitas, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Código da Receita')
    cod_produto = models.OneToOneField(Produtos, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Código do Produto')
    quantidade_produto_receita = models.IntegerField(verbose_name='Quantidade do Produto')



class Producao(models.Model):
    SITUACAO_PRODUCAO = [
        ('A', 'Aberto'),
        ('F', 'Fechado')
    ]
    cod_producao = models.SmallAutoField(primary_key=True, unique=True, verbose_name='Código da Produção')
    cod_receita = models.ForeignKey(Receitas, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Código da Receita')
    quantidade_producao = models.IntegerField(verbose_name='Quantidade de producação')
    status_producao = models.CharField(max_length=1, choices=SITUACAO_PRODUCAO, verbose_name='Status da Produção')
    data_hora_inicio = models.DateTimeField(default=timezone.now, verbose_name='Data do Inicio da Receita')
    data_hora_final = models.DateTimeField(verbose_name='Data de Finalização da Produção')



class Atualiza_Estoque_Producao(models.Model):
    ENTRADA_SAIDA = [
        ('E', 'Entrada'),
        ('S', 'Saida')
    ]

    cod_producao = models.OneToOneField(Producao, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Código da Producão')
    cod_produto = models.OneToOneField(Produtos, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Código do Produto')
    quantidade = models.IntegerField(verbose_name='Quantidade do produto')
    entrada_saida_produtos = models.CharField(max_length=1, choices=ENTRADA_SAIDA, verbose_name='Entrada ou Saida')




class Forma_Pagamento(models.Model):
    ESTILO_FORMA_PAGAMENTO_CHOICES = [
        ('A', 'A vista'),
        ('P', 'A prazo')
    ]

    cod_forma_pagamento = models.SmallAutoField(primary_key=True, unique=True, verbose_name='Código de Forma de Pagamento')
    nome_forme_pagamento = models.CharField(max_length=50, verbose_name='Nome da Forma de Pagamento')
    prazo_forma_pagamento = models.IntegerField(verbose_name='Prazo da Forma de Pagamento')
    estilo_forma_pagamento = models.CharField(max_length=1, choices=ESTILO_FORMA_PAGAMENTO_CHOICES, blank=True, null=True, default='', verbose_name='Tipo da Forma de Pagamento')

    def __str__(self):
        return self.nome_forme_pagamento


class Vendedor(models.Model):
    STATUS_VENDEDOR_CHOICES = [
        ('A', 'Ativo'),
        ('I', 'Inativo')
    ]

    cod_vendedor = models.SmallAutoField(primary_key=True, unique=True, verbose_name='Código do Vendedor')
    status_vendedor = models.CharField(max_length=1, choices=STATUS_VENDEDOR_CHOICES, blank=True, null=True, default='', verbose_name='Status do Vendedor')
    nome_vendedor = models.CharField(max_length=155, verbose_name='Nome do Vendedor')
    comissao_vendedor = models.FloatField(verbose_name='Comissão do Vendedor')
    def __str__(self):
        return self.nome_vendedor


class Pedido_Venda(models.Model):
    STATUS_PEDIDO_vENDA_CHOICES = [
        ('A', 'Aberto'),
        ('F', 'Fechado')
    ]
    cod_pedido_venda = models.SmallAutoField(primary_key=True, unique=True, verbose_name='Código do Pedido de Venda')
    status_pedido_venda = models.CharField(max_length=1, choices=STATUS_PEDIDO_vENDA_CHOICES, blank=True, null=True, default='A', verbose_name='Status do Pedido de Venda')
    data_pedido_venda = models.DateTimeField(default=timezone.now, verbose_name='Data do pedido')
    data_prazo_pedido_venda = models.DateTimeField(verbose_name='Prazo de entrega')
    cliente_pedido_venda = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, verbose_name='Cliente')
    vendedor_pedido_venda = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING, verbose_name='Vendedor')
    forma_pagamento_pedido_venda = models.ForeignKey(Forma_Pagamento, on_delete=models.DO_NOTHING, verbose_name='Forma de Pagamento')
    cod_titulo = models.ForeignKey(Titulo, on_delete=models.DO_NOTHING, verbose_name='Código do Titulo')


class Lista_Produtos_PedVen(models.Model):
    cod_pedido_venda = models.OneToOneField(Pedido_Venda, on_delete=models.CASCADE, verbose_name='Código do Pedido de Venda')
    codigo_produto_pedven = models.OneToOneField(Produtos, on_delete=models.DO_NOTHING, related_name='cod_item', verbose_name='Código do Produto')
    nome_produto_pedven = models.ForeignKey(Produtos, on_delete=models.DO_NOTHING, related_name='nome_item', verbose_name='Nome do Produto')
    valor_produto_pedven = models.ForeignKey(Produtos, on_delete=models.DO_NOTHING, related_name='valor_item', verbose_name='Valor do Produto')
    desconto_produto_pedven = models.ForeignKey(Produtos, on_delete=models.DO_NOTHING, related_name='desconto_item', verbose_name='Desconto do Produto')

