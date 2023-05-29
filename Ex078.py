# Faça om programa que leia 5 numros e guarde em uma lista
# No final motre qual foi o maior e o menor valor digitado
# e suas respectivas posições na lista.
lista = []
mn = m = pos = pm = 0
for l in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
    if l == 1:
        m = lista[l]
        mn = lista[l]
    else:
        if lista[l] > m:
            m = lista[l]
        if lista[l] < mn:
            mn = lista[l]
for p, v in enumerate(lista):
    if v == m:
        pos = p + 1
    if v == mn:
        pm = p + 1
print(f'Os números digitados foram {lista}\nO Maior valor foi {m} na posição {pos}\n'
      f'O menor foi {mn} na posição {pm}')
