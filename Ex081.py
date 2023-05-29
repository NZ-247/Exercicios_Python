# Crie um programa que vai ler varios numeros e colocar em uma lista
# A) quantos numeros foram digitados
# B) A lista de valores ordenados de forma decrescente
# Se o valor 5 foi digitadp e está na lista.
lista = []
while True:
    lista.append(int(input('Informe valores: ')))
    p = ' '
    while p not in 'NS':
        p = str(input('Deseja continuar? [S/N]: ')).strip()[0].upper()
        if p not in 'NS':
            print('Resposta \033[4;33minválida!\033[m Tente novamente.')
    if p == 'N':
        break
    lista.sort(reverse=True)
print(f'{"--¨¨" * 30}\nPrograma Finalizado!\nForam digitados {len(lista)} Elementos.\nOs Valores Digitados em ordem decrescente foram: \n{lista}')
if 5 in lista:
    print(f'O número \033[31m5\033[m foi digitado {lista.count(5)} vezes!')
