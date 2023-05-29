# faça um programa que leia o nome de quatro alunos e mostre a ordem sorteada.
from random import shuffle
print('Digite o \033[4mnome\033[m de \033[4;34mquatro\033[m \033[1;36malunos\033[m para saber a ordem de apresentação:')
a = str(input(''))
b = str(input(''))
c = str(input(''))
d = str(input(''))
list = [a, b, c, d]
shuffle(list)
print(f'A ordem dos alunos que vão \033[4;31apagar\033[m o quadro é :\n{list}')
'''print(lista)'''
