# crie um programa que faça o computador
# jogar Jokeipô com você
from time import sleep
from random import randint
from emoji import emojize

print(f'''{"Jankenpô":=^40}
Escolha um número para jogar:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
j = int(input(' '))
i = ('Pedra', 'Papel', 'tesoura')

c = randint(0, 2)
print('JAN')
sleep(1)
print('KEN')
sleep(1)

print('Pô!!!')
print('--==-' * 20)
print(emojize(f':man: Jogador escolheu {i[j]}'))
print(emojize(f':fire: O computador escolheu {i[c]}'))
print('-==--' * 20)
if c == 0:
    if j == 0:
        print('Empate')
    elif j == 1:
        print('\033[33mJogador Venceu!\033[m')
    elif j == 2:
        print('\033[36mComputdor Venceu \033[31m hahahahahaha1\033[m')
    else:
        print('JOGADA INVÁLIDA!')
elif c == 1:
    if j == 0:
        print('\033[33mComputador venceu! \033[31m hahahahahaha \033m')
    elif j == 1:
        print('\033[34mEmpate\033[m')
    elif j == 2:
        print('\033[32mJogador Venceu!\033[m')
    else:
        print('Jogada Imválida!')
elif c == 2:
    if j == 0:
        print('\033[35mJogador Venceu!\033[m')
    elif j == 1:
        print('\033[32mComputador Venceu! \033[31m hahahahahaha \033[m')
    elif j == 2:
        print('\033[1;33mEmpate!\033[m')
    else:
        print('Jogada Inválida!')
2
