# Faça um programa que jogue Par ou impar com o computador
# O jogo será interrompido quando o jogador perder
# Mostrando o total de vitótias consecutivas que ele conquistou até o final do jogo
print(f'{"Jogo do Par ou Ímpar":=^40}')
from random import randint
'''vu = vc = 0
while True:
    o = str(input('Ímpar ou Par?'))
    if o == 'Par':
        oc = 'Impar'
    else:
        oc = 'Par'

    user = int(input('Jogue um número:'))
    comp = randint(1, 10)
    soma = user + comp
    if soma % 2 == 0:
        soma = 'Par'
    else:
        soma = 'Impar'

    print(f'Você escolheu {user}, Computador escolheu {comp}, {user} + {comp} = {user + comp}')
    if o == soma:
        vu += 1
        print('O Jogador venceu!')
    elif oc == soma:
        vc += 1
        print('O Computador venceu!')
    p = str(input('quer continuar? [S/N]')).upper()
    if p == 'N':
        break
print(f'Fim do Jogo Você ganhou {vu} vezes e \033[3;36mPERDEU\033[m {vc}.')'''

v = count = d = 0
while True:
    jogador = int(input('Digite um valor:'))
    comput = randint(0, 10)
    total = jogador + comput
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par Ou Ìmpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {jogador}, Computador jogou {comput}')
    print('Deu par' if total % 2 == 0 else 'Deu Ímpar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você \033[31mPerdeu!\033[m')
            d += 1
    elif tipo == 'I':
        if total % 2 == 1:
            print('\033[36mVocê Venceu!\033[m')
            v += 1
        else:
            print('Você \033[31mPERDEU!\033[m')
            d += 1
    parar = str(input('Que Continuar? [S/N]')).upper().strip()[0]
    if parar == 'N':
        break
    count += 1
print(f'\033[4;35mGAME OVER!\033[m Foram {v} Vitótias e {d} \033[4;36mDERROTAS\033[m')
