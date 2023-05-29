# Crie um programa que leia  Nome, sexo e idade de várias pessoas
# Guardando os dados de cada pessoa em um dicionário e todos os DICTS em ima lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A Média de idade do grupo
# C) Uma lista com todas as pessoas com idade acima da média
# D) Quantia de mulheres cadastradas.
cadastros = []
soma = media = 0
while True:
    dados = {}
    dados['Nome'] = str(input('Nome: ')).title()
    dados['idade'] = int(input('idade: '))
    dados['sexo'] = str(input('sexo: [M/F]')).upper().strip()
    while dados['sexo'] not in 'MF':
        print('Resposta \033[33mInválida\033[31m!\033[m Digite apenas S ou F!')
        dados['sexo'] = str(input('Sexo: [M/F]')).upper().strip()
    cadastros.append(dados)
    p = str(input('Adicionas mais um dado? [S/N]')).upper().strip()
    while p not in 'SN':
        print('Resposta \033[33mInválida\033[31m!\033[m Digite apenas S ou N!')
        p = str(input('Adicionas mais um dado? [S/N]')).upper().strip()
    if p == 'N':
        break
for i in cadastros:
    soma += i['idade']
media = soma//len(cadastros)
print(f'\033[4;36m{"Cadastros Finalizados!":=^36}\033[m')
print(f'Total de Cadastros: {len(cadastros)}\nMédia de idade: {media}\nPassoas Acima da média:')
for v in cadastros:
    if v['idade'] > media:
        print(f'\033[4m{v["Nome"]} com {v["idade"]} anos\033[m')
print(f'As Mulheres cadastradas foram: ', end='')
for m in cadastros:
    if m['sexo'] == 'F':
        print(f'{m["Nome"]}', end=', ')
