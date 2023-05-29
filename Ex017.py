''' faça um programa que leia o cumprimeto do cateto opsto e do adjacente de um triãngulo retangulo, calcule e mostre o cumprimento da hipotenusa.'''
# co = float(input('Qual é a medida do cateto oposto? '))
# ca = float(input('Qual a medida do cateto adjacente? ' ))
# h = ((co*co)+(ca*ca))**(1/2)
# print(f'O valor da Hipotenusa é {h:.2f}')#
from math import hypot
co = float(input('Cumprimento do cateto oposto: '))
ca = float(input('Cumprimento do cateto adjacente: '))
print(f'O cumprimento da Hipotenusa é {hypot(co,ca):.2f}')
