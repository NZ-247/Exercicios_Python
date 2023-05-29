# Escreva um progrsma que faça o computador  "pensar" em um número inteiro entre 0 e 5 e peça ao usuário que tente descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário acertou ou não.
from random import randint
from emoji import emojize
from time import sleep
n = randint(0, 9)
print('-=-'*20)
print('Estou pensando em um número de 0 à 9.\nDúvido você acertar...')
print('-=-'*20)
u = int(input('Qual é o número que pensei? '))
print('Processando...')
sleep(3)
if u == n:
     print(emojize("Aeee, Acertou parça :thumbs_up:"))
else:
     print(f"O computador Venceu!\nO número é {n}")
