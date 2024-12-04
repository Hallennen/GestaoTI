from django.test import TestCase
import datetime
# Create your tests here.

# data = datetime.date.month(2)
# print(data)

data_atual = datetime.datetime.now()
nome_mes = data_atual.strftime("%B")
print(nome_mes)

# data_inicio = datetime.datetime(2022, 1, 1)
# data_fim = datetime.datetime(2022, 12, 31)

# diferenca = data_fim - data_inicio
# dias = diferenca.days