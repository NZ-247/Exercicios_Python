# desenvolva um programa que pergunte a distância de uma viajem em Km.
# calcule o preço da viajem, cobrando R$:0,50 por km para viajens de até 200Km
# E R$:0,45 para viagens mais longas.
v = float(input('Quantos Km serão percorridos na sua viajem? '))
if v < 200:
    print(f'O valor da passagem será de R${v*0.50}')
else:
    print(f'O valor da passagem será de R${v*0.45} por causa da promoção')
