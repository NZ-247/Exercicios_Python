# Crie um programa que leia vários números inteiros pelo teclado. O Programa só vai parar quando
# O usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando o flag).
c = s = 0
p = int(input('Digite um Número [Pare ao digitar 999]: '))
while p != 999:
    c += 1
    s += p
    p = int(input('Digite um Número [Pare ao digitar 999]: '))
print(f'Fim Do Programa\nForam digitados {c} Números, a soma de todos eles é de {s}.')
