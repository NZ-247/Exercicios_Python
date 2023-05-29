# Aprimore o Desafio 093 para que ele funcine com vários jogadores
# Incluindo um sistema de visualização de detalhes do aproveitamento de cada jogos
SAP = []
soma = 0
while True:
    jogadores = {}
    gols = []
    jogadores['nome'] = str(input('Nome do Jogador: ')).title()
    p = int(input('quantas partidas ele jogou? '))
    for j in range(p):
        g = int(input(f'Quantos gols na {j+1}° Partida? '))
        soma += g
        gols.append(g)
    jogadores['gols'] = gols[:]
    jogadores['total'] = soma
    soma = 0
    SAP.append(jogadores)
    parar = str(input('Adicoinar mais algum jogador? [S/N]')).upper().strip()[0]
    while parar not in 'SN':
        parar = str(input('\033[4;31mErRo: Responda apenas S ou N!\033[m\nAdionar mais algum jogador? ')).upper().strip()[0]
    if parar == 'N':
        break
print(f'{"=="*20}\n{"N°":<4} |{"Jogador":<12} |{"Total Gols":>10}\n{"=="*20} ')
for i, v in enumerate(SAP):
    print(f'{i:<4} |{v["nome"]:<12} |{v["total"]:>10}')
cd = str(input('ver desempenho dos Jogadores? [S/N]')).upper().strip()[0]
while cd not in 'SN':
    cd = str(input('\033[4;31mERRO! Digite apenas S ou N!\033[m\nver desempenho dos Jogadores? [S/N]')).upper().strip()[0]
if cd == 'S':
    while True:
        dt = int(input('Digite o Número do Jogador: [digite -1 para sair.] '))
        if dt == -1:
            break
        elif 0 > dt or dt > len(SAP):
            print(f'\033[4;31mERRO!\033[m Digite um Número entre 0 e {len(SAP)-1}')
        elif SAP[dt] in SAP:
            print(f'Jogador: {SAP[dt]["nome"]}')
            for i, v in enumerate(SAP[dt]["gols"]):
                print(f'{v} Gols na {i + 1} Partida')
print(f'\n\033[4;34m<<<Finalizado!>>>\033[m')
