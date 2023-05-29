# faça um programa que leia o peso de cinco pessoas.
# No final, mostre o maior e o menor peso lidos.
m = 0
mn = 0
for c in range(0, 6):
    p = float(input(f'Digite o peso da {c+1}° pessoa: '))
    if c == 1:
        m = p
        mn = p
    else:
        if p > m:
            m = p
        if p < mn:
            mn = p
print(f'O Maior peso fornecido foi {m}Kg.\nO Menor peso registado foi {mn}Kg.')
