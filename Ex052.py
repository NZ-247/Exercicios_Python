# Faça um programa que leia um número inteiro e diga se ele é um número primo.
n = int(input('Digite um Número e veja se ele é primo: '))
tot = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[36m', end='')
        tot += 1
    else:
        print(f'\033[33m ', end='')
    print(f'{c} ', end='')
print(f'\n \033[35mO número {n} foi divesível {tot} vezes\033[m.')
if tot == 2:
    print('E por isso ele \033[32mé um número primo')
else:
    print('E por isso ele \033[33mNão é um número primo')
