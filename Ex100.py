# Faça um Programa que tenha uma lista chamada números que possua duas Funções
# Uma será chamada sorteio e outra SomaPar
# A função sorteio irá sortear 5 números e colocá-los em uma lista
# a função soma irá somar os números paras da lista de números sorteados.
from time import sleep
from random import randint


def sorteio():
    sorteios = []
    for c in range(5):
        sorteios.append(randint(0, 100))
    somapar = []
    soma = 0
    print('Os valores sorteados foram:', end=' ')
    for n in sorteios:
        print(n, end=' ')
        sleep(0.3)
    print()
    sleep(1)
    for c in sorteios:
        if c % 2 == 0:
            somapar.append(c)
            soma += c
    print(f'Os números pares sorteados foram {somapar}, sua Soma resulta em {soma}.')


sorteio()
