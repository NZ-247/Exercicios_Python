# faça um programa que mostre na tela uma Contagem regressiva para o estouro de fogos de artifício
# indo de 10 até 0, com pausa de 1 segundo entre eles.
from emoji import emojize
from time import sleep
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print(emojize(f'Pá párápápápÁ'))
sleep(1.4)
print('POW')