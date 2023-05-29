def filex(arquivo):
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        print(f'Arquivo {arquivo} não encontrado!')
        return False
    else:
        print(f'Arquivo {arquivo} encontrado com sucesso!')
        return True


def criarArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro ao criar um arquivo!')
    else:
        print(f'Arquivo {nome} Criado com sucesso ;)')


'''def lerArquivo(nome):
    global a
    try:
        a = open(nome, 'rt')
    except:
        print(f'Erro ao ler o arquivo! :(')
    else:
        print(f'Cadastro Pessoas\n{"-"*30}')
        print(a.read())
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
    finally:
        a.close()'''


'''def lerArquivo(nome):
    try:
        a = open(nome, 'rt', encoding='utf-8')
    except FileNotFoundError:
        print('Arquivo não encontrado!')
    except Exception as e:
        print(f'Erro ao ler o arquivo: {e}')
    else:
        print(f'Cadastro Pessoas\n{"-"*30}')
#        print(a.read())
 #       a.seek(0)  # Retorna ao início do arquivo
        for linha in a:
            dado = linha.split('→')  # Use o mesmo separador usado na gravação
            dado[1] = dado[1].replace('\n', '')
            # Faça algo com os dados lidos, como imprimir na tela
            print(f'Nome: {dado[0]} ------→ Idade: {dado[1]}')
    finally:
        a.close()'''


def lerArquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'rt', encoding='utf-8') as arquivo:
            print(f'Cadastro Pessoas\n{"-"*30}')
            for linha in arquivo:
                dado = linha.strip().split('→')

                nome = dado[0]
                idade = dado[1]
                print(f'Nome: {nome} Idade: {idade}')
    except FileNotFoundError:
        print('Arquivo não encontrado!')
    except Exception as e:
        print(f'Erro ao ler o arquivo: {e}')
