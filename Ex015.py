# Exercício 15
a = int(input('Por quantos \033[4;33mdias\033[m o carro foi \033[4;34malugado\033[m? '))
p = float(input('Quantos \033[1;33mKm\033[m foram percorridos durante este período? '))
print(f'O \033[4;31mvalor\033[m do \033[1;36maluguel\033[m é de R$\033[1;32m{(60*a)+(0.15*p)}\033[m')
