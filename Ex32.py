# Faça um programs que leia um ano qualquer e mostre se ele é um ano bissexto.
from datetime import date
a = int(input('Que ano quer analisar? Para analisar o seu ano atual digite 0. '))
if a == 0:
    a = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0 :
    print(f'{a} É um ano bissesto.')
else:
    print(f'{a} não é Bissesto. ')
