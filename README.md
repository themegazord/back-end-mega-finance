# API - Banco de dados Megafinance | :hammer_and_wrench: In Building

# Objetivo

Esse readme tem como objetivo principal auxiliar os desenvolvedores mobile e front-end a como consumirem a API tanto local, quanto em produção.

## Instalação do MySQL Workbench

Para utilizar da API local e ter acesso ao banco de dados, você irá ter que instalar o MySQL Workbench, ou outro manipulador de banco de dados MySQL. Você pode baixar o MySQL Workbench clicando **[aqui](https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-community-8.0.29.0.msi)**

Caso precise de um tutorial de como configurar, clique **[aqui](https://www.youtube.com/watch?v=zpssr3u1EO8)** 
> Todos os direitos aos criadores do vídeo.


**Observação:**

*Ao configurar o MySQL Workbench, configure-o como:*

1. Usuário: megad3v
2. Senha: superonze02!
3. Nome do banco de dados: db_mega_finance
4. Porta: 3306
5. Host: 127.0.0.1


## Instalações do Back-end

Após você ter ou clonado, ou dado _fork_ no repositório extraído em sua máquina, você irá abrir seu terminal dentro da pasta e dar os seguintes comandos:

- Para criar o ambiente virtual no seu arquivo:
```
python -m venv venv
```
- Para habilitar o ambiente virtual:
```
venv\Scripts\activate
```
- Para instalar todos os componentes do requirements.txt
```
pip install -r requirements.txt
```
- Para rodas todas as migrações pendentes para o banco de dados.
```
python manage.py migrate
```

## Usuabilidade

Para ligar o servidor:

```
python manage.py runserver
```

Com o servidor ligado, basta consumir suas api's.

## API's

### **Guia para as API's**

1. [`Listagem dos Clientes`](#listagem-de-clientes)
2. [`Cadastro de Cliente`](#cadastro-de-clientes)
3. [`Detalhes do Cliente`](#detalhes-do-cliente)
4. [`Listagem dos Fornecedores`](#listagem-de-fornecedor)
5. [`Cadastro de Fornecedor`](#cadastro-de-fornecedores)
6. [`Detalhes do Fornecedor`](#detalhes-do-fornecedor)
7. [`Listagem dos Titulos`](#listagem-de-titulos)
8. [`Cadastro de Titulo`](#cadastro-de-titulo)
9. [`Detalhes do Titulo`](#detalhes-do-titulo)
10. [`Listagem do Contas a Pagar`](#listagem-do-contas-a-pagar)
11. [`Cadastro de Contas a Pagar`](#cadastro-de-contas-a-pagar)
12. [`Detalhes do Contas a Pagar`](#detalhes-do-contas-a-pagar)
13. [`Listagem do Contas a Receber`](#listagem-contas-a-receber)
14. [`Cadastro do Contas a Receber`](#cadastro-de-contas-a-receber)
15. [`Detalhes do Contas a Receber`](#detalhes-do-contas-a-receber)


## Listagem de Clientes

Metodos = **[GET]**

Link: http://127.0.0.1:8000/megafinance/clientes/api/

Exemplo de retorno de um usuário

```
    {
        "cod_cliente": 1,
        "status_cliente": "A",
        "tipo_cliente": "F",
        "nome_completo_cliente": "Gustavo de Camargo Campos",
        "cpf_cliente": "05081039160",
        "cnpj_cliente": null,
        "telefone1_cliente": null,
        "telefone2_cliente": "67981590619",
        "rua_endereco_cliente": "Rua Lúcia dos Santos",
        "numero_endereco_cliente": "1140",
        "cep_cliente": "79075104",
        "complemento_endereco_cliente": null,
        "bairro_endereco_cliente": "Parque do Sol",
        "email_cliente": "contato.wanjalagus@outlook.com.br"
    },
```


## Cadastro de Clientes

Metodos = **[POST]**

Link: http://127.0.0.1:8000/megafinance/envia-cliente/api/

### **Campos para POST**

```
    {
        "status_cliente": ,
        "tipo_cliente": ,
        "nome_completo_cliente": ,
        "cpf_cliente": ,
        "cnpj_cliente": ,
        "telefone1_cliente": ,
        "telefone2_cliente": ,
        "rua_endereco_cliente": ,
        "numero_endereco_cliente": ,
        "cep_cliente": ,
        "complemento_endereco_cliente": ,
        "bairro_endereco_cliente": ,
        "email_cliente": 
    }
```

### **Observações**

### **Campos de escolha**

Os campos status_cliente e tipo_cliente terão 2 possibilidade:
```
    STATUS_CLIENTES = [
        ('A', 'Ativo'),
        ('I', 'Inativo')
    ]

    TIPO_CLIENTE_CHOICES = [
        ('F', 'Pessoa Fisica'),
        ('J', 'Pessoa Juridica')
    ]

```



### **Campos obrigatórios**

1. Nome do Cliente
2. Endereço
3. Número do endereço
4. CEP
5. Bairro


```
{
    "cpf_cliente": [
        "cliente com este CPF já existe."
    ]
}
```

<br>


## Detalhes do cliente.

Link: http://127.0.0.1:8000/megafinance/detalhe-cliente/api/**id_do_cliente**/

Metodos: **[GET], [PATCH], [DELETE]**


<br>


## Listagem de Fornecedores

Metodos: **[GET]**

Link: http://127.0.0.1:8000/megafinance/fornecedores/api/

Exemplo de retorno:

```
    {
        "cod_fornecedor": 2,
        "status_fornecedor": "A",
        "tipo_fornecedor": "F",
        "nome_fornecedor": "Bernardo e Liz Entregas Expressas ME",
        "cpf_fornecedor": null,
        "cnpj_fornecedor": "99.073.177/0001-85",
        "telefone1_fornecedor": "(14) 3938-7755",
        "telefone2_fornecedor": "(14) 98541-2820",
        "rua_endereco_fornecedor": "Rua Santa Lúcia",
        "numero_endereco_fornecedor": "294",
        "cep_fornecedor": "17032-140",
        "complemento_endereco_fornecedor": null,
        "bairro_endereco_fornecedor": "Jardim Redentor",
        "email_fornecedor": "estoque@bernardoelizentregasexpressasme.com.br"
    }

```

## Cadastro de Fornecedor

Metodo: **[POST]**

Link: Link: http://127.0.0.1:8000/megafinance/envia-fornecedor/api/

### **Campos para POST**

```
    {
        "status_fornecedor": ,
        "tipo_fornecedor": ,
        "nome_fornecedor": ,
        "cpf_fornecedor": ,
        "cnpj_fornecedor": ,
        "telefone1_fornecedor": ,
        "telefone2_fornecedor": ,
        "rua_endereco_fornecedor": ,
        "numero_endereco_fornecedor": ,
        "cep_fornecedor": ,
        "complemento_endereco_fornecedor": ,
        "bairro_endereco_fornecedor": ,
        "email_fornecedor": 
    }
```

### **Observações**

### **Campos de escolha**

Os campos status_fornecedor e tipo_fornecedor terão 2 possibilidade:
```
    STATUS_FORNECEDORES_CHOICES = [
        ('A', 'Ativo'),
        ('I', 'Inativo')
    ]

    TIPO_FORNECEDOR_CHOICES = [
        ('F', 'Pessoa Fisica'),
        ('J', 'Pessoa Juridica')
    ]
```

### **Campos obrigatórios**

1. Nome do Cliente
2. Endereço
3. Número do endereço
4. CEP
5. Bairro

Caso dado POST em um fornecedor que já tem CNPJ ou CPF cadastrado, 400 será retornado com a seguinte mensagem

```
{
    "cpf_cliente": [
        "cliente com este CPF já existe."
    ]
}
```



## Detalhes do Fornecedor

Metodo: **[GET][PATCH][DELETE]**

Link: http://127.0.0.1:8000/megafinance/detalhe-fornecedor/api/**codigo_do_fornecedor**


### **Particulariedades do DELETE**

Foi implementado uma validação no DELETE, caso o fornecedor que foi solicitado a deleção, será validado se o mesmo tem algum vinculo com titulos a pagar dentro do sistema, se estiver com vinculo, retornará a API retornará 404 e a seguinte mensagem ("Fornecedor tem Titulo Vinculado") que poderá ser trocada para mostrar para o usuário futuramente 

## Listagem de Titulos

Metodo: **[GET]**

Link: http://127.0.0.1:8000/megafinance/titulos/api/

### **Exemplo de Retorno**

```
    {
        "cod_titulo": 2,
        "status_titulo": "A",
        "descricao_titulo": "Compra de catupiry",
        "pagar_receber_titulo": "P",
        "data_inicio_titulo": "2022-05-24T11:42:38-04:00",
        "data_final_titulo": null
    }
```

## Cadastro de Titulo

Metodo: **[POST]**

Link: Link: http://127.0.0.1:8000/megafinance/envia-titulo/api/

### **Campos para POST**

    {
        "status_titulo": ,
        "descricao_titulo": ,
        "pagar_receber_titulo": ,
        "data_inicio_titulo": ,
        "data_final_titulo": 
    }

### **Peculiariedades do POST**

Pode ou não ser passado o parametro data_inicio_titulo, caso seja enviado, o servidor irá encaminhar ao banco de dados o que foi enviado, se não for enviado, o servidor pegará a data INSERT ao inserir na tabela.

data_final_titulo aceita null, então, se o cliente não informar nada, deverá ser encaminhado null ao servidor, do contrário, encaminhado o que for passado como parametro.

### **Campo Obrigatórios**

1. Descrição do titulo

## Detalhes do Titulo

Metodo: **[GET][PATCH][DELETE]**

Link: http://127.0.0.1:8000/megafinance/detalhe-titulo/api/**codigo-do-titulo**


## Listagem do Contas a Pagar

Metodo: **[GET]**

Link: http://127.0.0.1:8000/megafinance/contas_a_pagar/api/

### **Exemplo de Retorno**

```
    {
        "cod_contas_a_pagar": 4,
        "valor_titulo_a_pagar": 200,
        "valor_desconto_a_pagar": 0,
        "nome_fornecedor_contas_a_pagar": 2,
        "cod_titulo": 2
    }
```

### **Peculiaridades do GET**

Tanto fornecedor quanto o código do titulo virão apenas com a PK do elemento em sua determinada tabela. Para pegar essas informações, deverá ser consumido duas API's
1. [`Detalhes do Fornecedor`](#detalhes-do-fornecedor)
2. [`Detalhes do Titulo`](#detalhes-do-titulo)

Ambas, você passará o PK que vier, nessas API para obter os dados de cada qual.

### **Observação**

Tanto essa, quanto a API de Contas a Receber, deverão aparecer na mesma tela, com os mesmo dados, pois uma vai ser atrelada a outra.


### Cadastro de Contas a Pagar

Metodo: **[POST]**

Link: http://127.0.0.1:8000/megafinance/envia-contas_a_pagar/api/

### **Campos para o POST**

```
    {
        "valor_titulo_a_pagar": ,
        "valor_desconto_a_pagar": ,
        "nome_fornecedor_contas_a_pagar": ,
        "cod_titulo": 
    }
```

### **Campos Obrigatórios**

1. Código do Fornecedor
2. Valor do Titulo
3. Codigo do Titulo

## Detalhes do Contas a Pagar

Metodo: **[GET][PATCH][DELETE]**

Link: http://127.0.0.1:8000/megafinance/detalhe-contas-a-pagar/api/**codigo_do_contas_a_pagar**


## Listagem Contas a Receber

Metodo: **[GET]**

Link: http://127.0.0.1:8000/megafinance/contas-a-receber/api/

### **Exemplo de retorno**
```
    {
        "cod_contas_a_receber": 1,
        "nome_cliente_contas_a_receber": 1,
        "cod_titulo": 6,
        "valor_titulo_a_receber": 800,
        "desconto_titulo_a_receber": 0
    }
```

## Cadastro de Contas a Receber

Metodo: **[POST]**

Link: http://127.0.0.1:8000/megafinance/envia-contas-a-receber/api/

### **Campos para o POST**

```
    {
        "cod_contas_a_receber": ,
        "nome_cliente_contas_a_receber": ,
        "cod_titulo": ,
        "valor_titulo_a_receber": ,
        "desconto_titulo_a_receber": 
    }
```

### **Campos Obrigatórios**

1. Código do Cliente
2. Código do Titulo
3. Valor do Titulo


## Detalhes do Contas a Receber

Metodo: **[GET][PATCH][DELETE]**

Link: http://127.0.0.1:8000/megafinance/detalhe-contas-a-receber/api/**codigo-contas-a-receber**

## License
[MIT](https://choosealicense.com/licenses/mit/)