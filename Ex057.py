# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "m" ou "f".
# Caso esteja errado peça a digitação novamente até ter um valor correto.
'''s = ''
while s != 'M' and s != 'F':'''
s = str(input('Digite seu Sexo: [M/F] ')).strip().upper()[0]
while s not in 'MF':
    s = str(input('Qual o seu sexo? [M/F]: ')).upper().strip()[0]
    if s != 'M' and s != 'F':
        print('Opção \033[31minválida\033[m, tente \033[33mnovamente!\033[m')
if s == 'M':
    print('Olá senhor.\nSeja muito bem vindi ao meu Programa;)')
else:
    print('Olá senhorita:)')
