# m6-s2-teste-backend-gatione

## Instruções

Primeiramente clone o repositório para uma pasta local

Dentro do repositório crie o venv (bash: `python -m venv venv`)

Ative o ambiente no terminal (bash: `source venv/Scripts/activate`)

Instale as dependências (bash: `pip install -r requirements.txt`)

Rode o server localmente (bash: `./manage.py runserver`)

Para abrir a interface de upload acesse a rota localhost (`http://localhost:8000/`), escolha o arquivo e aperte em postar.

Para ver todas as transações acesse a rota `http://127.0.0.1:8000/api/transactions/`

Para postar uma nova transação envie a seguinte estrutura no corpo da requisição:

```
{
    "type": "1",
    "date": "2022-11-25",
    "value": "11",
    "cpf": "12345678901",
    "card": "21312",
    "hour": "2022-11-25 12:30",
    "owner": "Example",
    "shop": "Example's shop"
    "sign": "-"
}
```

Para ver as transações de uma loja em específico e seu saldo atual acesse a rota: `http://127.0.0.1:8000/api/transactions/<nome da loja>/`, exemplo: `http://127.0.0.1:8000/api/transactions/Example's shop/`
