# Exercício 12
v = float(input('Qual o valor do produto?R$:'))
d = float(input('De quntos % será o desconto? '))
print(f'O \033[1;31mPreço\033[m do produto com \033[1;33m{d}\033[m% de \033[1;32mdesconto\033[m será de: R$\033[1;36m{v-(d*v)/100}\033[1;m')
