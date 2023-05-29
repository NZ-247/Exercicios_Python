

def nameValid():
    '''
    Essa função serve para validar nomes,
    funciona de forma semelhante ao input()
    Porém não aceita números.
    :return: Nome válido, sem números entre as letras.
    '''

    entrada = input("Nome: ").title().strip()
    while entrada.isdigit():
        entrada = input("Erro! O nome deve conter apenas letras, sem números. Tente novamente: ")
    return entrada


def idValid():
    '''
    Essa função serve para validar idades,
    não permitindo que o usuário digite
    letras.
    :return: Idade do usuário válida, sem letras.
    '''
    while True:
        entrada = input("Idade: ").strip()
        if entrada.isdigit():
            return int(entrada)
        else:
            print("Erro! Digite apenas números. Tente novamente.")


def inf(list1, list2):
    '''
    Esta função mostra em forma de tabelas duas listas,
    onde uma faz referência a outra, Ex: Nome e idade de usuários
    :param list1: Primeira lista, ou lista de itens.
    :param list2: Segunda lista, ou lista de quantidade.
    :return:
    '''

    print(f'Nome: {"Idade":->12}')
    for c in range(len(list2)):
        print(f'\033[1;32m{list1[c]}\033[33m{"-"*(10-(len(list1[c])))}→\033[1;35m{list2[c]:>4}\033[m')


'''def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        with open(arq, 'at') as a:
            a.write(f'{nome}→{idade}')

    except FileNotFoundError:
        print('Arquivo não encontrado!')
    except PermissionError:
        print('Permissão para acesssar o arquivo negada!')
    except Exception as e:
        print(f'Houve um erro ao tentar escrever no arquivo!: {e} ')'''

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        with open(arq, 'at', encoding='utf-8') as a:
            a.write(f'{nome}→{idade}\n')

    except FileNotFoundError:
        print('Arquivo não encontrado!')
    except PermissionError:
        print('Permissão para acessar o arquivo negada!')
    except Exception as e:
        print(f'Houve um erro ao tentar escrever no arquivo!: {e}')

'''arq = 'teste.txt'
if not arquivo.filex(arq):
    arquivo.criarArq(arq)
cadastrar(arq, 'maria', 30)'''
