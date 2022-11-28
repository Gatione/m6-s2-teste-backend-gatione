from django.db import models

# Create your models here.


class Transaction(models.Model):

    type = models.CharField(max_length=50)
    date = models.DateField()
    value = models.FloatField()
    cpf = models.IntegerField()
    card = models.CharField(max_length=12)
    hour = models.DateTimeField()
    owner = models.CharField(max_length=14)
    shop = models.CharField(max_length=19)
    sign = models.CharField(max_length=1)
