# Faça um programa que tenha uma Função área()
# Receba as dimencões (largura e cumprimento)
# Mostre a área do terreno.
def Area(cumprimento, largura):
    a = cumprimento * largura
    print(f'A Área Total do Terreno de {cumprimento}x{largura} é de {a:.2f}M².')


print(f'{"Gerênciador de terrenos":=^36}')
ctrn = float(input('Cumprimento Do Terreno: '))
ltrn = float(input('Largura do Terreno: '))
Area(ctrn, ltrn)
