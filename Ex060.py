# Faça um programa que leia um número qualquer e mostre seu fatorial.
n = int(input('Digite um número inteiro e veja o seu fatorial: '))
c = n
f = 1
'''while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)'''

'''from math import factorial
n = int(input('Digite um número inteiro e veja seu fatorial: '))
print(f'O Fatorial de {n} é {factorial(n)}')'''


for c in range(n, 0, -1):
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)
