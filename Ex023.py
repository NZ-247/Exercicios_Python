# Crie um programa que leia um númeoro de 0 à 9999 e mostre na tela cada um dos dígitos separados.

n = int(input('Digite um número de 0 à 9999: '))
print(f'Unidades: \033[1;31m{n // 1 % 10}')
print(f'Dezenas: \033[1;32m{n // 10 % 10}')
print(f'Centenas: \033[1;33m{n // 100 % 10}')
print(f'Milhar: \033[1;34m{n // 1000 % 10}')
