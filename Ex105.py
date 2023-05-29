# Faça um programa que pode receber várias notas de alunos e vai retornar
# Um dicionário com as seguintes informações
# - Quantidade de motas
# - A maior nota
# - A menor nota
# - A Média da turma
# - A Situação(opcinal)
# Adicione também docstrings da função.


"""def analise(notas):
    '''
    :param notas: Esse Parâmetro recebe as notas dos alunos e faz uma Análise,
        Revelando assim a quantia de notas dos alunos, a maior e a menor nota da lista,
        juntamente com a média e situação da turma,
        alucando essas informações em dicionário e mostrando ao fim.
    :return: Sem Retorno
    '''
    dcn = {}
    maior = mn = me = 0
    for i, n in enumerate(notas):
        if i == 0:
            maior = n
            mn = n
        else:
            if n > maior:
                maior = n
            if n < mn:
                mn = n
        me += n
    me = me/len(notas)
    dcn['Registros'] = len(notas)
    dcn['Maior nota'] = maior
    dcn['mn'] = mn
    dcn['Media'] = me
    if me <= 40:
        dcn['Situação da Turma'] = '\033[1;31mPéssima!\033[m'
    elif 40 < me < 60:
        dcn['Situação da Turma'] = '\033[1;33mRegular!\033[m'
    elif 60 < me <= 70:
        dcn['Situação da Turma'] = '\033[1;34mBoa Até.\033[m'
    else:
        dcn['Situação da Turma'] = '\033[1;36mUm Pouco nais que Boa, Dá pra melhorar!\033[m'
    for p, v in dcn.items():
        print(f'{p}: {v}')

lista = []
while True:
    nome = str(input('Nome do Aluno: ')).title().strip()
    lista.append(int(input(f'Média das notas de {nome}: ')))
    p = str(input('Adicionar mais dados?')).upper()
    while p not in 'SN':
        p = str(input('\033[4;33mERRO!\033[1;33m Digite "S" para "Sim" e "N" Para Não: \033[m'))
    if p == 'N':
        break
analise(lista)"""
#Resolucão do professor:


def notas(*n, sit=False):
    """
    --> Função para analisar notas e situação de vários alunos.
    :param n: uma ou mais notas de alunos.
    :param sit: valor opcinal que mostra ou não a situação da turma.
    :return: Dicionário com informacões sobre a situação da turma.
    """
    r = dict()
    r['Total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 70:
            r['situação'] = 'Boa'
        elif r['media'] >= 5:
            r['situação'] = 'Regular'
        else:
            r['situação'] = 'Péssima'
    return r


resp = notas(25, 78, 65, 98, 56, sit=True)
print(resp)
help(notas)