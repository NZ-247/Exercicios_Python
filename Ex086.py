# Crie um programa que crie uma matriz de dimenção 3x3
# Preencha os valores lidos pelo teclado
# No final, mostre a Matriz na tela com a formatação correta.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(3):
        matriz[l][c] = int(input(f'Insira um valor para a posição [{l}, {c}]: '))
print('>' * 25)
for l in range(3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
