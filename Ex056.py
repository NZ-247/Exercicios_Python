# Desenvolva um programa que leia o nome,idade e sexo de 4 pessoas.
# No final do programa mostre:
# A Média de idade do grupo.
# Qual o nome do homem mais velho.
# Quantas mulheres tem menos de 20 anos.
hv = 0
m = 0
nv = ''
m20 = 0
mi = 0
for c in range(1, 5):
    print(f'{"-"*10}{c}° Pessoa{"-"*10}')
    n = str(input('nome: ')).strip().title()
    i = int(input('Idade: '))
    s = str(input('Sexo [H/M]: ')).upper().strip()
    m += i
    me = m/4
    if c == 1 and s in 'H':
        hv = i
        nv = n
    if s in 'H' and i > hv:
        hm = i
        nv = n
    if s in 'M' and i < 20:
        m20 += 1
print(f'A média de idade do grupo é {mi}\nO homem mais velho é o {nv} com {hv} anos de idade.\nE são {m20} Mulhores '
      f'com menos de vinte anos.')
