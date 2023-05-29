# Faça um programa que leia nome e peso de várias pessoas
# No Final Mostre:
# A) Quantas pessoas foram cadastradas
# B) Uma Listagem com as pessoas mais pesadas
# C) Uma Listagem com as pessoas mais leves.
dados = []
mp = pl = 0
dado = []
while True:
    dado.append(str(input('Digite o nome: ')))
    dado.append(int(input('Informe o peso: ')))
    dados.append(dado[:])
    dado.clear()
    parar = str(input('Realizar outro cadastro? [S/N]')).upper().strip()[0]
    while parar not in 'NS':
        print('Resposta Inválida! Digite "S" para (Sim) e "N" para (Não).')
        parar = str(input('Realizar outro cadastro? [S/N]')).upper().strip()[0]
    if parar == 'N':
        break
for c, v in enumerate(dados):
    if c == 0:
        pl = mp = v[1]
    else:
        if v[1] >= mp:
            mp = (v[1])
        elif v[1] <= pl:
            pl = (v[1])
print(f'{"--¨¨" * 30}\n'
      f'\033[4;36mPrograma Finalizado!\033[m\n'
      f'Foram Cadastradas {len(dados)} Pessoas.\n'
      f'o Maior peso foi {mp}Kg, peso de:')
for p in dados:
    if p[1] == mp:
        print(p[0])
print(f'{"--" * 20}\n'
      f'Enquanto o peso mais Live foi {pl}Kg, peso de:')
for p in dados:
    if p[1] == pl:
        print(p[0])
