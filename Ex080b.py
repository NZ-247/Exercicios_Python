# Função enumarate, essa Função percorre a lista com índices, ou seja, posição e valor de cada elemrnto.
'''valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na Posição {c} encontrei o valor {v}!')
print('Cheguei no final da lista.')'''
# No python há uma peculiaridade, quando uma variável recebe uma lista
# Elas ficam conectadas, tudo que for alterado em uma mudará na outra
# Para copiar uma lista sem que fiquem interligadas basta fazer a lista 'b' recerber a 'a' do começo ao fim
a = [2, 1, 54, 6, 34, 96]
b = a[:]
b[3] = 36
print(f'Lista A: {a}\nLista B: {b}')
