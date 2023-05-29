# Crie um programa que leia um número real pelo teclado e mostre sua porção inteira
'''from math import trunc
v = float(input('Digite um valor com ponto flutuante (número com casas décimais): '))
# print(f'O valor digitado foi {v} e sua parte inteira é {math.trunc(v)}')
print(f'O valor digitado foi {v} e a sua parte inteira é {trunc(v)}')'''
n = float(input('Digite um valor com casas décimais: '))
print(f'O \033[1;36mvalor\033[m digitado foi \033[4;33m{n}\033[m e sua parte \033[4;34minteira\033[m é \033[1;35m{int(n)}\033[m')
