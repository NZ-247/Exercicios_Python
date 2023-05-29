# crie um programa que mostre na tela
# Todos os números pares que estão no intervalo desejado.
print('Defina um intervalo e veja os numero pares presentes nele:')
p = int(input('Início:'))
s = int(input('Fim: '))
for c in range(p, s+1):
    if c % 2 == 0:
        print(c, end=' ')
