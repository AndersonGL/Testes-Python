import requests
import datetime


data2 = datetime.date.today()  # solitando a biblioteca dia, mês e ano atual.
url2 = "https://economia.awesomeapi.com.br/last/USD"   # api gratuita

response = requests.get(url2)  # fazendo requisções http

dados = response.json() # manipulação de dados

preco_atual_dolar = "{:.2f}".format(float(dados['USDBRL']['high']))

print('O Dolar(USA) está no valor: R$', preco_atual_dolar, '(', data2, ')')


# Fazer a inversão de data para 26/02/2025

