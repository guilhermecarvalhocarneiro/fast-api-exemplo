# Projeto FastAPI

## Pré requisitos

Faça o clone desse projeto para o diretório


Acesse o diretório criado na etapa anterior
```console
  cd fastapi-to-do 
```

Crie e habilite um ambiente python
```console
  python -m venv venv
```
```console
  source venv\Script\activate | windows
  . venv/bin/activate | linux e macOs
```
Instale as dependências do projeto

```console
  pip install -r requirements.txt
```

Crie o arquivo .env

```console
  cp .env.example .env
```

Insira os dados do seu banco no arquivo .env

## Uso

Rode o servidor:
```console
uvicorn main:app --reload
```

O servidor estará disponível em: 
```
http://localhost:8000
```

## Rotas

Todas as rotas estão disponíveis nas urls:  /docs ou /redoc, com Swagger or ReDoc.

## Estrutura do projeto
-----------------

As partes da aplicação são:

::

    fastapi-to-do
    ├── core              - app de configuração do projeto.
    │   ├── api - endpoints principais.
    │   ├── config       - arquivo de configuração.
    │   |── cruds       - arquivo com crud padrão a ser herdados.
    |   |── database       - arquivo de configuração  do banco de dados.
    |   └── security       - arquivos de configuração de seguranca.
    ├── authentication              - app com todas as rotas relacionadas ao usuário.
    │   ├── api - endpoints da app.
    │   ├── cruds       - cruds para interacao com o banco de dados.
    │   |── models       - models da app.
    |   |── schemas       - schemas a serem usados nas rotas.
    |   └── security       - arquivos de configuração de seguranca.
    ├── migrations               - app relacionada as migrations da aplicação.
    │   ├── versions   - migrations geradas para o banco de dados.
    │   └── env - arquivo de configuração das migrations.
    ├── .env.example        - arquivo com as configurações locais da aplicação.
    └── main.py          - FastAPI aplicação e configuração do servidor.