# Escreva um programa que leia um Número n inteiro qualquer
# mostre na tela os n primeiros termos elementos de uma sequência de Fibonacci.
print(f'{"sequência de Fibinacci":=^40}')
f1 = 1
f2 = 0
t = int(input('Quantod termos da sequência de Fibonacci você quer ver? ')) - 1
t2 = 0
while t2 <= t:
    f3 = f2 + f1
    f1 = f2
    f2 = f3
    t2 += 1
    print(f3, '→', end=' ')
print('Fim')
