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
```bash
python -m venv venv
```
- Para habilitar o ambiente virtual:
```bash
venv\Scripts\activate
```
- Para instalar todos os componentes do requirements.txt
```bash
pip install -r requirements.txt
```
- Para rodas todas as migrações pendentes para o banco de dados.
```bash
python manage.py migrate
```

## Usuabilidade

Para ligar o servidor:

```bash
python manage.py runserver
```

Com o servidor ligado, basta consumir suas api's.

## API's

Listagem de Clientes
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


Cadastro de Clientes
Metodos = **[POST]**

Link: http://127.0.0.1:8000/megafinance/clientes/api/

**Observações**

**Campos de escolha**

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



**Campos obrigatórios**

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


Consulta detalhada de clientes.

Link: http://127.0.0.1:8000/megafinance/detalhe-cliente/api/**id_do_cliente**/

Metodos: **[GET], [PATCH], [DELETE]**



## License
[MIT](https://choosealicense.com/licenses/mit/)