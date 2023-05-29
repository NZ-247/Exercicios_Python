# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços
# No final mostre uma listagem de preços organizando os dados em forma de tabula.
print(f'\033[4;33m{" " * 50}\n\n\033[0;36m{"NZ° T.E.C":^50}\033[4;33m\n{" " * 50}\033[m')
itens = ('Ram', 1300, 'ssd', 1250, 'notebook', 5000, 'Placa de vídeo', 4000, 'monitor', 8000, 'HD', 300)
for pos in range(0, len(itens)):
    if pos % 2 == 0:
        print(f'\033[32m{itens[pos]:.<50}\033[m', end='R$ ')
    else:
        print(f'\033[33m{itens[pos]: >5.2f}\033[m')
