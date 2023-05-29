# Escreva um progrma leia a velocidade de um carro.
# Se ele ultrapassar um velocidade "X", mostre à ele um mensagem dizendo que ele foi multado.
# A multa será de R$:7,00 por cada km exedente.
v = float(input('Qual a velicidade do carro? '))
if v >= 80:
    print(f'Você foi multado em R${(v-80)*7:.2f}')
else:
    print('Parabéns, você é um ótimo motorista!')
