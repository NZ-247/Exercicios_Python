# Crie um programa que leia o Nome, ano de nascimento e carteira de trabalho
# cadastreos em um dicionário se por a CTPS for diferente de zero
# o dicionario recebe-rá também o ano de contratação e o salário.
# calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import date
dados = {}
ano = date.today().year
dados['nome'] = str(input('Digite o seu nome: ')).title()
dados['nascimento'] = int(input('Digite sua data de nascimento: '))
dados['idade'] = ano - dados['nascimento']
dados['carteira'] = int(input('Carteira de trabalho: '))
if dados['carteira'] >= 1000000:
    dados['contrato'] = int(input('Ano de contratação do primeiro emprego: '))
    dados['salario'] = int(input('De qunto era seu salário: '))
    dados['aposentadoria'] = (dados['contrato'] + 35) - (ano - dados['contrato'])
    dados['aposentadoria'] = dados["aposentadoria"] - ano
print(f'{"---+"*36}')
for c, i in dados.items():
    if c == 'aposentadoria':
        print(f'\033[1;36m{c} : \033[32m{i} anos\033[m')
    else:
        print(f'\033[1;36m{c} : \033[33m{i}\033[m')
