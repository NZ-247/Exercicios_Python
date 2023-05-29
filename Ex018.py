
# faça um programa que leia um ângulo qualquer e mostre seu seno ,cosseno e a tangente.
from math import sin, cos, tan, radians
a = float(input('Qual o \033[1;36mângulo\033[m? '))
print(f'O seno de {a} é {sin(radians(a)):.2f}\nO cosseno de {a} é {cos(radians(a)):.2f}\nA tangente de {a} é {tan(radians(a)):.2f}')
