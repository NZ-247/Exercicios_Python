# Crie um programa que tenha uma tupla com vários palávras(não usar acentos).
# Depois disso você deve mostrar para cada palavra quais são as suas vogais.
list = ('banana', 'limosine', 'mamão', 'barco', 'babalu', 'pirulito', 'fazenda')
for p in list:
    print(f'\nNa Palavra {p.upper()}, temos ', end='')
    for l in p:
        if l in 'aeiou':
            print(l, end=' ')
