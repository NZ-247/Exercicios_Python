# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# se o valor digitado for ímpar, desconsidere-o
count = 0
soma = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        soma += n
        count += 1
print(f'Você informou {count} Números Pares, o Resultado da soma dos mesmos foi {soma}')
