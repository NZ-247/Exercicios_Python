#  Crie um Programa que vai gerar cinco números aleatórios e colocar em uma tupla
#  Depois disso, mostre a listagem de números gerados e também indeique o Menor e o Maior valor que estão na tupla.

from random import randint
m = 0
mn = 0
print(f'{"Gerador de Númeoros":=^50}')
n = tuple(randint(0, 999) for i in range(5))
print(f'Os Números Sorteados foram {n}')
'''for c in range(5):
    if c == 0:
        m = mn = n[c]
    else:
        if n[c] > m:
            m = n[c]
        if n[c] < mn:
            mn = n[c]'''
print(f'O Menor Número gerado foi {min(n)}.\nO maior Número gerado foi {max(n)}.')
