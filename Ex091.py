# Crie um Programa onde 4 jogadores joguem um dado o temham resultados aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem,
# Sabendo que o vencedor tirou o maior número no dado.
from time import sleep
from random import randint
from operator import itemgetter
jogo = {'jogador 1': randint(1, 6,),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogodor 4': randint(1, 6)}
rank = list()
print('Valores Sorteados:')
for k, v in jogo.items():
    print(f'{k}: {v}')
    sleep(1)
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
sleep(3)
print(f'{"--*" * 20}')
for i, v in enumerate(rank):
    print(f'{i+1}° lugar: {v[0]} com {v[1]} pontos.')
