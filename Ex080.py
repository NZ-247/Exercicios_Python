# Crie um programa onde o usuário possa digitar cinco valores
# no final mostre a lista ordenada sem utilizar o sort().
valores = []
for item in range(0, 5):
    n = int(input('Digite um valor: '))
    if item == 0 or n > valores[-1]:
      valores.append(n)
      print('Adicionado ao Final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                print(f'Adicionado no posicão {pos}...')
                break
            pos += 1
print(f'{"-¨¨--" * 30}\nOs Valores digitados foram {valores}')
