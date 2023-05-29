# Crie um programa que leia vários números inteiros pelo teclado.
# Mostre a média entre todos os todos os valores e qual foi o maior e o menor valores lidos.
# todo O programa deve perguntar oa usuário se ele quer ou não Continuar a digitar os valores.
'''p = 10
m = ma = c = n1 = 0
o = ''
while p != 0:
    n = int(input('Digite um número: '))
    c += 1
    m += n
    p -= 1
    if n > n1:
        n1 = n
    if p == 0:
        o = str(input('Deseja continuar? [S/N]')).upper()
        while o != 'S' and o != 'N':
            print('Resposta inválida, escolha "S" ou "N"!')
            o = str(input('Deseja continuar? [S/N]')).upper()
        if o == 'N':
            p = 0
        elif o == 'S':
            p = 10
            print(f'Programa finalizado!\nA Média da soma dos valores digitados foram {m/c}\nO Maior número digitado foi {n1}')
'''
resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar [S/N]: ')).upper()
media = soma / quant
print(f'Foram Digitados {quant} Números, A Média entre eles foi {media}.\nO Maior Foi {maior} e o menor foi {menor}')
