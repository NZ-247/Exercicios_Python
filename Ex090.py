# Faça um programa que leia Nome e Média de um aluno
# Guardando também a situação em um Dicionário
# No final mostre o conteúdo da estrutura na tela.
dicionario = {}
notas = []
m = 0
dicionario['nome'] = str(input('Incira seu nome: ')).title()
for c in range(4):
    n = float(input(f'Qual sua no {c+1}° Bimestre? '))
    notas.append(n)
    m += n
dicionario['notas'] = notas
dicionario['media'] = m / 4
print(f'- Nome: {dicionario["nome"]}\n- Média {dicionario["media"]:.2f}')
if dicionario['media'] >= 7:
    print(f'- Sitiação: \033[1;36mAprovado!\033[m')
elif dicionario['media'] <= 5:
    print(f'- Situação: \033[1;31mReprovado!\033[m')
else:
    print(f'- Situação: \033[1;33mRecuperação!\033[m')
