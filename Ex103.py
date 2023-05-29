# Faça um programa com uma função chamada ficha que receba dois parâmetros opcinais
# o nome de um jogadosr e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não seja infomado


def ficha(jogador='<Desconhecido>', gols=0):
    print(f'O Jogador {jogador} fez {gols} Gols no Campionato!')


n = str(input('Nome do Jogador: '))
g = str(input('Gols marcados: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
