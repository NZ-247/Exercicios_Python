# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal,sabendo que ela não pode exeder 30% do salário ou então o empréstimo será negado.
e = float(input('valor da casa? R$'))
s = float(input('Salário do comptrador? R$'))
p = float(input('Quantos anos de financiamento? '))
if (s * 0.3) < (e / (p * 12)):
    print('Empréstimo \033[4;31mnegado!\033[m\nMotivo: O valor de cada parcela tem que ser inferior à 30% do salário.')
elif (s * 0.3) > (e / p):
    print(f'Empréstimo \033[4;36mAprovado!\033[m\nSua parcela será de R${e / p:.2f}')
