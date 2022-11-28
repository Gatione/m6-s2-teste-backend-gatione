from rest_framework import generics
from .serializers import TransactionSerializer
from .models import Transaction
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.encoding import smart_str
from rest_framework.views import Response


# from django.core.handlers.wsgi import WSGIRequest
# from django.http import FileResponse


class TransactionsView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects


class ShopTransactionsView(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        transactions = Transaction.objects.filter(shop=self.kwargs["shop"])
        balance = sum(
            [
                -transaction.value if transaction.sign == "-" else transaction.value
                for transaction in transactions
            ]
        )
        return transactions

    def get(self, request, *args, **kwargs):
        transactions = Transaction.objects.filter(shop=self.kwargs["shop"])
        balance = sum(
            [
                -transaction.value if transaction.sign == "-" else transaction.value
                for transaction in transactions
            ]
        )
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            {
                "transactions": serializer.data,
                "balance": balance,
            }
        )


def index(request):
    return render(request, "index.html")


def uploadFile(request):
    type = [
        None,
        "Débito",
        "Boleto",
        "Financiamento",
        "Crédito",
        "Recebimento Empréstimo",
        "Vendas",
        "Recebimento TED",
        "Recebimento DOC",
        "Aluguel",
    ]
    file = request.FILES["file"].readlines()
    listData = []
    for line in file:
        line = smart_str(line, encoding="utf-8")
        data = {
            "type": type[int(line[0])],
            "date": f"{line[1:5]}-{line[5:7]}-{line[7:9]}",
            "value": f"{int(line[9:19])/100}",
            "cpf": f"{int(line[19:30])}",
            "card": f"{line[30:42]}",
            "hour": f"{line[1:5]}-{line[5:7]}-{line[7:9]} {int(line[42:44])}:{int(line[44:46])}:{int(line[46:48])}",
            "owner": f"{line[48:62]}".strip(),
            "shop": f"{line[62:81]}".replace("\r", "").strip(),
            "sign": f"{'-' if (int(line[0]) == 2 or int(line[0]) == 3 or int(line[0]) == 9) else '+'}",
        }
        listData.append(data)
        transaction = Transaction.objects.create(**data)

    return HttpResponse(
        """<html><script>
        window.location.replace("/api/transactions/")
        </script></html>"""
    )
