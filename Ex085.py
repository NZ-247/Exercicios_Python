# Crie um programa onde o usuário possa digitar Sete valores numéricos
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem Crescente.
valores = [[], []]
n = 0
for c in range(0, 7):
    n = (int(input(f'Digite o {c+1}° valor: ')))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
valores[0].sort()
valores[1].sort(reverse=True)
print(f'{">"*40}\nPrograma Finalizado!\nOs Valores Pares Digitados Foram {valores[0]}\n'
      f'Os Valores Ímpares Digitados São: {valores[1]}')
