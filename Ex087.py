# Aprimore o desafio anterior, mostrando
# A) A soma de todos os valores Pares Digitados
# B) A Soma dos Valores da Terceira Coluna
# C) O Maior Valor da Segunda Linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = somac = maior = 0
for l in range(3):
    for c in range(3):
       matriz[l][c] = int(input(f'Insera um valor em [{l, c}]: '))
print(f'{">" * 40}')
for l in range(3):
    for c in range(3):
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if c == 2:
            somac += matriz[l][c]
        if l == 1:
           if c == 0 or matriz[l][c] > maior:
                   maior = matriz[l][c]
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma De Todos os valores pares é {soma}\n'
      f'A Soma dos valores da terceira coluna equivale à {somac}\n'
      f'O Maior valor da segunda linha é {maior}')
