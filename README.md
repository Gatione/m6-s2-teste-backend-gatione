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


# Documentação do CNAB

| Descrição do campo | Inicio | Fim | Tamanho | Comentário                                                                                                                |
| ------------------ | ------ | --- | ------- | ------------------------------------------------------------------------------------------------------------------------- |
| Tipo               | 1      | 1   | 1       | Tipo da transação                                                                                                         |
| Data               | 2      | 9   | 8       | Data da ocorrência                                                                                                        |
| Valor              | 10     | 19  | 10      | Valor da movimentação. _Obs._ O valor encontrado no arquivo precisa ser divido por cem(valor / 100.00) para normalizá-lo. |
| CPF                | 20     | 30  | 11      | CPF do beneficiário                                                                                                       |
| Cartão             | 31     | 42  | 12      | Cartão utilizado na transação                                                                                             |
| Hora               | 43     | 48  | 6       | Hora da ocorrência atendendo ao fuso de UTC-3                                                                             |
| Dono da loja       | 49     | 62  | 14      | Nome do representante da loja                                                                                             |
| Nome loja          | 63     | 81  | 19      | Nome da loja                                                                                                              |

# Documentação sobre os tipos das transações

| Tipo | Descrição              | Natureza | Sinal |
| ---- | ---------------------- | -------- | ----- |
| 1    | Débito                 | Entrada  | +     |
| 2    | Boleto                 | Saída    | -     |
| 3    | Financiamento          | Saída    | -     |
| 4    | Crédito                | Entrada  | +     |
| 5    | Recebimento Empréstimo | Entrada  | +     |
| 6    | Vendas                 | Entrada  | +     |
| 7    | Recebimento TED        | Entrada  | +     |
| 8    | Recebimento DOC        | Entrada  | +     |
| 9    | Aluguel                | Saída    | -     |
