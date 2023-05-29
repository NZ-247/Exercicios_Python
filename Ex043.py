# Desenvolva um lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# -Abaixo de 18.5: Abaixo do Peso    -Entre 18.5 e 25: peso ideal
# -25 até 30: Sobrepeso              -30 até 40: Obesidade
# -Acima de 40: Obesidade mórbida
m = float(input('Qual o valor de sua massa corpória? (Kg)'))
a = float(input('Digete a sua estura: (M) '))
p = m / a**2
print('Você está ', end='')
if p <= 18.5:
    print('\033[4;31mAbaixo do peso!\033[m')
elif 18.5 <= p < 25:
    print('Com \033[4;36mPeso Ideal.\033[m')
elif 25 <= p < 30:
    print('Com \033[4;37mSobrepeso\033[m!')
elif 30 <= p < 40:
    print('Com \033[4;33mObesidade!\033[m')
else:
    print('Com \033[4;31mObesidade Mórbida!\033[m')
print(f'{p:.2f}Kg')
