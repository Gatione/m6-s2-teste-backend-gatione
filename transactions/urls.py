from django.urls import path
from . import views

urlpatterns = [
    path("", views.TransactionsView.as_view()),
    path("<shop>/", views.ShopTransactionsView.as_view())
]