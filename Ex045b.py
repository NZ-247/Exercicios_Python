from time import sleep
from random import randint
from emoji import emojize


class JankenpoGame:
    def __init__(self):
        self.opcoes = ('Pedra', 'Papel', 'Tesoura')
        self.resultados = {
            (0, 0): 'Empate',
            (0, 1): '\033[33mJogador Venceu!\033[m',
            (0, 2): '\033[36mComputador Venceu!\033[m',
            (1, 0): '\033[33mComputador Venceu!\033[m',
            (1, 1): '\033[34mEmpate\033[m',
            (1, 2): '\033[32mJogador Venceu!\033[m',
            (2, 0): '\033[35mJogador Venceu!\033[m',
            (2, 1): '\033[31mComputador Venceu!\033[m',
            (2, 2): '\033[1;33mEmpate!\033[m'
        }

    def jogar(self):
        print(f'{"Jankenpô":=^40}')1
        print('Escolha um número para jogar:')
        print('[ 0 ] Pedra')
        print('[ 1 ] Papel')
        print('[ 2 ] Tesoura')
        j = int(input(' '))

        c = randint(0, 2)
        print('JAN')
        sleep(1)
        print('KEN')
        sleep(1)
        print('Pô!!!')
        print('--==-' * 20)
        print(emojize(f':man: Jogador escolheu {self.opcoes[j]}'))
        print(emojize(f':fire: O computador escolheu {self.opcoes[c]}'))
        print('-==--' * 20)

        resultado = self.resultados[(j, c)]
        print(resultado)


# Instanciar e jogar o jogo
jogo = JankenpoGame()
jogo.jogar()
