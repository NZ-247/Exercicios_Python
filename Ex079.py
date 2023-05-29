# Crie um programa onde o usuário possa digitar vários numeros e armazene em uma lista
# caso o mumero ja exista na lista nao sera adicionado
# NO final, serão axibidos todos os valores únicos digitados em ordem crescente.
print(f'{"*--"*10}\n{"Bloco de Notas Numérico"}\n{"*--"*10}')
lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    for item in lista:
        if lista.count(item) > 1:
            print('Valor já digitado! Não será adicionado à lista.')
            lista.pop()
    p = ' '
    while p not in 'SN':
        p = str(input('Deseja Continuar? [S/N]')).strip().upper()
    if p == 'N':
            break
lista.sort()
print(f'{"--¨¨"*30}\nOs Valores Digitados foram:\n{lista}')
