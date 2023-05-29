# Exercício 13
s = float(input('Qual o \033[4;33msalário\033[m do funcionário? R$:'))
a = float(input('De quantos % será seu \033[4;31maumento\033[m?'))
print(f'O \033[1;36mnovo\033[m salário do funcionário com \033[1;33m{a}\033[m% de \033[4;34maumento\033[m será de R$:\033[4;32m{s+a*s/100}\033[m')
