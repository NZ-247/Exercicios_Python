# Crie uma Tupla com os 20 primeiros colocados da tabela do campionato Brasileiro de Futebol na ordem de colocação
# Depois mostre:
# A) Apenas os 5 Primeiros colocados
# B) Os últimos 4 colocados
# C) Uma lista com os times em ordem alfabética
# D) Em que posição está o time do Vasco.

print(f'{"="*40}\n\033[4;33m{"Tabela do Brasileirão":^40}\033[m\n{"=" * 40}')


clubes = ['Palmeiras', 'Santos', 'Vasco',
          'Grêmio', 'Flamengo', 'Corinthians', 'Internacional',
          'Cruzeiro', 'São Paulo', 'Atlético-Mineiro', 'Botafogo',
          'Fluminence', 'Ccoritiba', 'Bahia', 'Goiás',
          'Portuguesa', 'Atlétivo-Paranaense', 'Vitóvia', 'Chapécoense', 'Cuiaba']

print('\033[2;36mOs três primeiros colocados são:\033[m')

for c in range(0, 3):
    print(f"{c + 1}° {clubes[c]}")

print(f'{"-+¨¨+-" * 40}\n\033[2;35mOs quatro últimos colocados são:\033[m')
for c in range(16, len(clubes)):
    print(f'{c+1}° {clubes[c]}')
print(f"{'-+¨¨+_' * 40}\n\033[2;34mOs Times da lista em ordem Alfabética ficam:\033[m")
for c in range(0, len(clubes)):
    print(f'{c + 1}° {sorted(clubes)[c]}')

'''print(f"{'='*50}\n\033[4;34mOs 5 primeiros coçocados são\033[m: \n{clubes[0:5]}\n"
      f"\033[4;31mOs 4 Últimos são\033[m:\n{clubes[-4:]}\n"
      f"\033[4;35mTimes em ordem alfabética\033[m:\n{sorted(clubes)}\n"
      f"\033[4;32mA Chapecoense está na \033[33m{clubes.index('Chapécoense')}ª\033[32m colocação.")'''
