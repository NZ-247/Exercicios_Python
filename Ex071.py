# Crie um programa que simule o funcionameto de um caixa eletrônico
# No início, pergunte ao usário qual será o valor a ser sacado(número interiro)
# O programa vai informar quantas cédulas de cada valor srão entregues
# OBS: Considere que o caixa possua cédilas de R$50, R$20, R$10, R$1
print(f'{"Caixa Eletrônico":=^40}')
'''while True:
    saque = int(input('O valor do saque será de: R$'))
    c1 = saque // 50
    c1b = saque % 50
    c2 = c1b // 20
    c2b = c1b % 20
    c3 = c2b // 10
    c3b = c2b % 10
    c4 = c3b // 1
    print('Serão sacados:')
    if c1 >= 1 and c1 != 0:
        print(f'{c1} Cédulas de R$:50')
    if c2 >= 1 and c2 != 0:
        print(f'{c2} Cédulas de R$:20')
    if c3 >= 1:
        print(f'{c3} Cédulas de R$:10')
    if c4 >= 1:
        print(f'{c4} Cédulas de R$:1')
    stop = ' '
    while stop not in 'SN':
        stop = str(input('Deseja fazer mais algum saque? [S/N]:')).upper().strip()[0]
        if stop != 'S' and stop != 'N':
            print('Opção inválida! Tente Novamente.')
    if stop == 'N':
        break
print(f'\033[4;33m{"-"*40}\n\033[4;36mPrograma Finalizado!Até uma Próxima.\033[4;35m\n{"="*40}')'''



valor = int(input('Que Valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        if ced == 20:
            ced = 10
        if ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('Programa Finalizado! Até a Próxima.')