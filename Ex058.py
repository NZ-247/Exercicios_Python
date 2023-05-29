# melhore o desafio 28 do jogo onde o computador vai "pensar" em um número entre 0 a 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
# quantos palpites foram nescessários para vencer.
from random import randint
from time import sleep
from emoji import emojize
n = randint(0, 20)
print(f'{"Teste Sua Sorte":=^35}')
sleep(1)
print(f'Sou um computador e vou pensar em um número de 0 à 20')
sleep(4)
print(f'E Você terá que acertá-lo.')
sleep(2)
print('Estou pensando em um Número ', end='')
sleep(1)
for c in range(1, 4):
    print('.', end='')
    sleep(1)
j = int(input('\nQual Número eu pensei? '))
t = 1
sleep(1)
while not j == n:
    t += 1
    if j < n:
        j = int(input(emojize('quase isso, um pouco mais ... Tenta de novo vai: ')))
    elif j > n:
        j = int(input(emojize('Quase isso, um pouco menos... Tenta de novo aí vai: ')))
sleep(2)
print(f'Certa resposta, você acertou com apenas {t} tentativas.')
