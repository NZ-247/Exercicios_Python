# Crie um programa que leia vários números inteiros pelo teclado. O Programa só vai parar quando
# O usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando o flag).

Soma = count = 0
while True:
    valor = int(input('Digite Um Valor [999 encerra o programa]: '))
    if valor == 999:
        break
    count += 1
    Soma += valor
print(f'Você Digitou {count} Números, a somas deles resulta em {Soma}.')
