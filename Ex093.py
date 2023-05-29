# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o Nome do jogador e quantas partidas ele jogou
# depois leia a quantia de gols marcados por ele em cada partida.
# Ao final, tudo isso será será guardado em um dicinário.
# Incluindo o total de gols feitos durante o campeonato
'''GAP = {}
soma = s = 0
GAP['jogador'] = str(input('Nome do jogador: ')).title()
jogos = int(input('Quantos Jogos ele competiu? '))
GAP['jogos'] = jogos
for i in range(jogos):
    s = int(input(f'Quantos gols na {i+1}° partida?'))
    GAP[f'Gols na {i+1}° partida'] = s
    soma += s
GAP['Gols total'] = soma
print(f'{"---+"*36}')
for k, v in GAP.items():
    print(f'{k} : {v}')'''
gerente = dict()
soma = 0
gols = list()
gerente['Nome'] = str(input('Nome do Jogador: ')).title()
f = int(input('Quantas partidas ele competiu? '))
for c in range(f):
    n = int(input(f'Quantos gols ele marcou na {c+1}° partida? '))
    gols.append(n)
    soma += n
gerente['gols'] = gols[:]
gerente['total'] = soma
print(f'{"---+"*36}\n{gerente}\n{"---+"*36}')
for k, v in gerente.items():
    print(f'O campo {k} tem valor {v}')
print(f'+=+='*36)
for c, v in enumerate(gerente['gols']):
    print(f'→ Na partida {c+1}, marcou {v} Gols')
print(f'Foram marcados {gerente["total"]} Gols no Total')
