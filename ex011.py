# Exercício 11
l = float(input('Qual a largura da parede? '))
a = float(input('Qual a altura da parede? '))
print(f'A dimenção da parede é \033[1;33m{l}\033[m X \033[1;34m{a}\033[m.\nCom Área de \033[1;35m{l*a}\033[mm².\nSerá necessário \033[1;32m{(l*a)/2}\033[m Litros de tinta para pintar a parede.')
