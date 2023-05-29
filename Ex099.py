# Faça um programa que tenha uma função chamada maior()
# Que recebe vários parâmetros com valores inteiros
# seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep


def maior(*valores):
    m = 0
    for c in valores:
        if c >= m:
            m = c
    sleep(2)
    print(f'{"--"*25}\nAnalizando os valores...')
    for c in valores:
        print(c, end=' ')
        sleep(0.3)
    print(f'foram passados {len(valores)} valores\n'
          f'O maior número informado foi {m}')


maior(2, 5, 3, 6, 7, 1)
maior(8, 4)
maior(2, 3, 5, 1, 9, 7, 6)
