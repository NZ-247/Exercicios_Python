# crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras MAIÚSCULAS.
# - O nome com todas as letras minúsculas.
# - Quantas letras tem ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.
n = str(input('Digite o seu nome completo: ')).strip()
print(f'Olá {n.capitalize()}\nOi {n.title()}\nanalisando deu nome...\nSeu nome apenas em maiúsculas fica {n.upper()}.')
print(f'E com letras munúsculas {n.lower()}.')
print(f'Ele tem \033[1;36m{len(n) - n.count(" ")}\033[m letras.')
d = n.split()
print(f'Seu primeiro nome é \033[1;33m{d[0]}\033[m\nEle possui \033[1;34m{len(d[0])}\033[m letras.')
print(n.find(' '))
s = n.split()
print(f'Seu nome tem {len(s[0])}')
