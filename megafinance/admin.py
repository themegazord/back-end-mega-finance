from django.contrib import admin

from .models import *


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cod_cliente', 'nome_completo_cliente', 'tipo_cliente', 'cpf_cliente', 'status_cliente')
    list_display_links = ('cod_cliente', 'nome_completo_cliente')
    search_fields = ('nome_completo_cliente',)
    list_filter = ('status_cliente',)
    list_editable = ('status_cliente',)
    list_per_page = 10



class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('cod_fornecedor', 'nome_fornecedor', 'tipo_fornecedor', 'cnpj_fornecedor', 'status_fornecedor')
    list_display_links = ('cod_fornecedor', 'nome_fornecedor')
    search_fields = ('nome_fornecedor',)
    list_filter = ('status_fornecedor',)
    list_editable = ('status_fornecedor',)
    list_per_page = 10



class TituloAdmin(admin.ModelAdmin):
    list_display = ('cod_titulo', 'descricao_titulo', 'pagar_receber_titulo', )
    list_display_links = ('cod_titulo',)
    list_per_page = 10


class ContasAPagarAdmin(admin.ModelAdmin):
    list_display = ('cod_contas_a_pagar',)
    list_display_links = ('cod_contas_a_pagar',)
    list_per_page = 10


class ContasAReceberAdmin(admin.ModelAdmin):
    list_display = ('cod_contas_a_receber', )
    list_display_links = ('cod_contas_a_pagar', )
    list_per_page = 10

class GrupoProdutosAdmin(admin.ModelAdmin):
    list_display = ('cod_grupo', 'nome_grupo')
    list_display_links = ('cod_grupo', 'nome_grupo')
    search_fields = ('nome_grupo', )
    list_per_page = 10
    






admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(Titulo, TituloAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Contas_A_Pagar, ContasAPagarAdmin)
