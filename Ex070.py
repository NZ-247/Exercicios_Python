# Crie um programa que leia o nome e o preço de vários produtos
# O Programa deverá peruntar se o usuário vai continuar.
# No Final mostre:
# A) Qual é o total gasto na compra.

# B) Quantos produtos custam mais de R$1000.

# C) Qual é o nome do produto mais barato.
print(f'\033[33m{"NZ STORE":=^40}\033[m')
gasto = p1 = count = mn = 0
pb = np = ' '
while True:
    p = str(input('Nome do Produto: '))
    valor = float(input('Preço do Produto R$:'))
    gasto += valor
    if valor >= 1000:
        p1 += 1
    count += 1
    if count == 1:
        mn = valor
    else:
        if valor < mn:
         mn = valor
         np = p
    parar = str(input('Deseja Adicinar algo à mais? [S/N]')).upper().strip()[0]
    if parar == 'N':
        break
print(f'\033[33m{"-"*40}\033[m\nO valor total da compra foi de {gasto}\nDentre os produtos comprados {p1} custam menos de R$1000\nO produto {np} foi o barato')
