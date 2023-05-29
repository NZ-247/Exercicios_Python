# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O Programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
# Para cada jogo, cadastrando tudo em uma lista composta.
print(f'{"=" * 40}\n{"PALPITES MEGA SENA":^40}\n{"=" * 40}')
from random import randint
from time import sleep
jogos = int(input('Quantos Jogos quer gerar? '))
apostas = []
n = []
num = 0
for c in range(jogos):
    count = 0
    while True:
        num = randint(1, 60)
        if num not in n:
            n.append(num)
            count += 1
        if count >= 6:
            break
    n.sort()
    apostas.append(n[:])
    n.clear()
for p, a in enumerate(apostas):
    print(f'{p+1}° Jogo: {a}')
    sleep(1)
print(f'\033[4;35mPrograma Finalizado!')
