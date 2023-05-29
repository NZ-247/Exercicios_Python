# Um Professor quer sortear um de quatro alunos para apagar o quadro.faça um programa que ajude ele a fazzer esse sorteio.
print('Digite o nome dos quatro alunos:')
p =input('\033[1;33m1°\033[m- ')
d =input('\033[1;35m2°\033[m- ')
t =input('\033[1;34m3°\033[m- ')
q =input('\033[1;36m4°\033[m- ')
from random import choice
lista = [p, d, t, q]
print(f'O \033[1;33mescolhido\033[m para \033[1;31mapagar\033[m o quadro foi \033[4;32m{choice(lista)}\033[m')


