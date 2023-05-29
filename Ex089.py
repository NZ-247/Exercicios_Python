# Crie um Programa que leia nome e Duas Notas de vários alunos e Guarde tudo em uma lista composta
# Mostre um boletim contendo a média de cada um
# Permita que o usuário possa mostrar as notas de cada aluno individualmente.
alunos = list()
dados = []
media = 0
while True:
    nome = str(input('Nome do Aluno: ')).title()
    dados.append(nome)
    for c in range(4):
        n = float(input(f'Informe a {c+1}° nota: '))
        dados.append(n)
        media += n
    media = media/4
    dados.append(media)
    alunos.append(dados[:])
    dados.clear()
    media = 0
    parar = str(input('Adicinar mais um aluno? [S/N]')).upper().strip()[0]
    while parar not in 'SN':
        parar = str(input('\033[4;33mReposta Inválida!\033[m Tente Novamente.\nAdicinar mais um Aluno? ')).upper().strip()[0]
    if parar == 'N':
        break

while True:
    ver = str(input('Deseja ver a nota de Algum Aluno? [S/N]')).upper().strip()[0]
    while ver not in 'SN':
        ver = str(input(f'\033[4;33mResposta Inválida!\033[m Tente Novamente.\n'
                        f'Deseja ver a nota de algum aluno? [S/N]')).upper().strip()[0]
    if ver == 'S':
        print(f"{'-'*30}\n{'N°':<4}{'NOME':<10}{'MÉDIA':>8}\n{'-'*30}")

        for p, i in enumerate(alunos):
            print(f'{p:<4}|{i[0]:<10}|{i[5]:>8.1f}')
    else:
        break
    visun = int(input('Insira o número do aluno para ver suas notas: '))
    print(f'As Notas de \033[1;34m {alunos[visun][0]} \033[m Foram: \n{alunos[visun][1:5]}\nSua média Foi \033[32m{alunos[visun][5:]}\033[m\n{">---> " * 10}')
print(f'{">>>"*10}{"<<<"*10}\n\033[4;35mPrograma Finalizado!')
