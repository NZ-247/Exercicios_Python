# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal à condição de pagamento:
# -à vista dinheiro/cheque: 10% de desconto   - em até 2x no cartão: preço normal
# -à vista no cartão:5% de desconto     -3x ou mais no cartão:20% de juros
print(f'{" Loja do NZ° ":=^40}')
t = float(input('Qual o valor da compra? R$:'))
f = float(input('Selecione uma das opções:\n[1] À vista no dinheiro/cheque: \n[2] À Vista no catão: \n[3] 2x no cartão: \n[4]Mais opções de parcelamento no cartão: \n '))
if f == 1:
    print(f'você ganhou em desconto de 10% nesta compra, de R${t} sairá por R${t - (t*0.1)}.')
elif f == 2:
    print(f'Você ganhou um desconto de 5% em nossa loja, de R${t} sairá por R${t - (t*0.05)}.')
elif f == 3:
    print(f'Em 2x no cartão, cada parcela custará R${t/2:.2f}, Não serão cobrados juros.')
elif f == 4:
    j = int(input('Parcalamos em até 10x no cartão, porém serão cobrados até 20% de juros.\nEm quantas vezes irá parcear? '))
    if 5 > j >= 3:
        print(f'Serão {j} Parcelas de R${(t+(t*0.05))/j:.2f}')
    elif 7 > j >= 5:
        print(f'Serão {j} Parcelas de R${(t+(t*0.1))/j:.2f}')
    elif 7 <= j < 10.1:
        print(f'Serão {j} Parcelas de R${(t+(t*0.2))/j:.2f}')
else:
    print('Opção \033[4;31minválida\033[33m!\033[m\nReinicie o programa de escolha uma opção entre [1, 2, 3 ou 4.')
