# Crie um programa que leia dois valores e moste um menu na tela:
# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos Números
# [5] Sair de programa
# Seu Programa deverá realizar a operação solicitada em cada caso.
print(f'{"Calculadora":=^20}')
n1 = float(input('Digite um Valor: '))
n2 = float(input('Digite outro Número: '))
op = 0
while op != 5:
    print('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do Programa
    ''')
    op = int(input('>>>>>Qual é sua Opção: '))
    if op == 1:
        print(f'A Soma de {n1} + {n2} é {n1 + n2}')
    elif op == 2:
        print(f'{n1} x {n2} = {n1 * n2}')
    elif op == 3:
        m = 0
        if n1 > n2:
            m = n1
        else:
            m = n2
            print(f'O Maior é {m}')
    elif op == 4:
        n1 = float(input('Novo Valor 1: '))
        n2 = float(input('Novo valor 2: '))
    else:
        print('Opção inválida! Tente Novamente.')
    if op != 5:
        b = 'O que quer fazer agora?'
    elif op == 5:
        b = ""
    print('-*-=' * 40)
    print(b)
print('Fim Do Programa! Até Mais:)')
