# desenvolva um programa que leia i comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-=-'*20)
print('Analisador de triângulos')
print('-=-'*20)
print('Digite em metros, o valor da medida de três retas e veja se é possivel criar um triângulo com elas:')
c1 = float(input('Comprimento 1: '))
c2 = float(input('Cumprimento 2: '))
c3 = float(input('cumprimento 3: '))
if c3 + c2 > c1 and c2 + c1 > c3 and c3 + c1 > c2:
    print('Sim é possivel formar um triângulo.')
else:
    print('Não é possível formar um triângulo.')
