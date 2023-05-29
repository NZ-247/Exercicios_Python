# crie um programa que leia e armazene valores em uma lista
# depois disso, crie duas listas extras
# uma para valores pares e outra para ímpares respctivamente
# Ao final, mostre o conteúdo das três listas geradas.
lista1 = []
par = []
impar = []
while True:
    n = int(input('Insira Um Valor: '))
    lista1.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    p = str(input('Gostaria de Prosseiguir? [S/N]')).upper().strip()[0]
    while p not in 'NS':
        print('resposta \033[33mInaválida!\033[m Tente Novamente.')
        p = str(input('Gostaria de continuar? [S/N] ')).upper().strip()[0]
    if p == 'N':
        break
print(f'{"--¨¨" * 35}\n\033[4;35mPrograma Finalizado!\033[m\nOs Valores informados Foram {lista1}\n '
      f'Os Pares Foram: \n{par}\n'
      f'Os ìmpares foram: \n{impar}')
