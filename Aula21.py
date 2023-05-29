# Interactive help:
# A Ajuda interativa do Python serve como uma grande biblioteca com manuais de todas as funções.
# para acessá-la basta digitar 'help' no console python, para fecha-la utilize o comando 'quit'
help(input)
# docstrings:
# Semelhante ao help ele tráz informações sobre o metodo
# para utiliza-lo basta dar print('metodo'__doc__)Ex:
print(input.__doc__)
# Outra maneira de funcinalidade das docstrings é fazer um nanual para uma função criada por você:


def media(*valores):
    '''

    :param valores: Valores que serão somandos e dividos para obter as médias.
    :return: sem retorno
    '''
    me = 0
    for n in valores:
        me += n
    me = me/len(valores)
    print(f'\nA Média dos valores {valores} é {me}')


media(98, 87, 96, 92)

# Parâmetros Opcinais:
#   São parãmetros que recebem valor 0 caso não sejam chamados, dessa forma a função não da erro na execução


def soma(a=0, b=0, c=0):
    s = a+b+c
    print(f'\nA Soma Vale {s}')


soma(45, 67)
soma(21, 45, 89)
soma()
# Escopo de Variáveis:
#   local onde uma variavel vai existir e onde vai deixar de existir
#   Há dois tipos, as variáveis de escopo local e global
#Ex:


def teste(b):
    a = 9
    b += 6
    c = 3
    print(f'\nA dentro vale {a}\n'
          f'B dentro vale {b}\n'
          f'C dentro vale {c}')


a = 5
teste(a)
print(f'A fora vale {a}')
# Retorno de resultados.
#   uma função pode retornar um valor para quem a chamou usando a palavra chave "return"
#   é retornado para o ponto onde a função foi chamada, essa funcionalidade permite excutar o função e personalizar o resoltado


def quadrado(valor):
    return valor ** 2


q1 = quadrado(9)
q2 = quadrado(6)
q3 = quadrado(3)
print(f'\nO Quadrado de 9, 6, 3 é respectivamente {q1} {q2} {q3}.')
