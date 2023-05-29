# Faça um Programa que tenha uma Função chamada contador()
# ele terá que receber três parâmetros: inicio, fim e passo e realize a contagem
# seu programa tem que realizar três contagens através da função criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contaagem personalizada.
from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} com passo {passo}')
    sleep(2.5)
    if inicio < fim:
        count = inicio
        while count <= fim:
            print(f'{count}', end=' ')
            sleep(0.5)
            count += passo
        print('Fim')
    else:
        count = inicio
        while count >= fim:
            print(f'{count}', end=' ')
            sleep(0.5)
            count -= passo
        print('Fim')


print(f'{"Contador":=^36}')
contador(1, 10, 1)
contador(10, 0, 2)
i = int(input('Personalise uma contagem\nDefina um inicio:'))
f = int(input('Defina o fim: '))
p = int(input('Defina o passo: '))
contador(i, f, p)
