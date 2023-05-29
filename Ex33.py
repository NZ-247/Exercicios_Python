# Faça um programa que leia três números e diga qual é o maior e o meonor deles.
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))
'''if v1 < v2 > v3:
    print(f'O Número {v2} é o maior digitado.')
if v3 < v1 > v2:
        print(f'O Número {v1} é o maior digitado.')
if v1 < v3 > v2:
    print(f'O Número {v3} é o maior digitado.')
if v1 > v2 < v3:
    print(f'E o Menor é o {v2}.')
if v3 > v1 < v2:
    print(f'E o Menor é {v1}.')
if v1 > v3 < v2:
    print(f'E o Menor é {v3}.')'''
m = v1
if v2 > v1 and v2 > v3:
    m = v2
if v3 > v1 and v3 > v2:
    m = v3
mn = v1
if v2 < v1 and v2 < v3:
    mn = v2
if v2 > v3 and v1 > v3:
    mn = v3
print(f'O maior número digitado foi {m}.\nE o Menor foi {mn}. ')
