# Faça um programa que calcule a soama entre todos os
# Números ímpares que são múltiplos de três e estejam no intervalo de 1 à 500.
print('Defina um intervalo e veja a soma de apenas os números ímpares presentes nele\nque são múltiplos de três:')
c = int(input('Início: '))
f = int(input('Fim: '))
count = 0
soma = 0
for i in range(c, f+1):
    if i % 2 != 0 and i % 3 == 0:
        count += 1
        soma += i
print(f'A soma apenas dos {count} valores soicitados é {soma}')
