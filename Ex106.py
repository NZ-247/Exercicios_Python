# faça um mini-sistema que utilize o interactive help do python
# O usuário vai digitar o comado e o Manual vai aparecer
# quando o usuário digitar a palavra fim, o programa se encerra-rá
# OBS: Use cores.
from time import sleep


def PyHelp(funcao):
    """
    Essa função é um mini-sistema que utiliza o interactive help do Python
    Basta Digitar o nome de uma função, Biblioteca ou Método que desejar e
    o manual do mesmo irá ser mostrado
    um pequeno detalhe que ter que estar atento é que, para acessar o manual de um
    método é nescessário digitat "str." antes do método. Ex: str.upper
    caso contrário dará erro.
    :param funcao: Função que deseja ver o manual
    :return: Manual da Função, biblioteca ou método informado.
    """
    return help(funcao)


c = PyHelp
while True:
    print(f'\033[1;42mSistema de Ajuda PyHelp')

    if c == 'sair':
        break
    print(f'\033[1;33;40m{"~~"*36}\n{"Acessando o Manual do Comando":^36} "{c}"\n{"~~"*36}')
    for i in range(3):
        print(".", end='')
        sleep(1)
    print(f'\033[1;30;44m{PyHelp(c)}')
    c = str(input('\033[mFunção ou biblioteca > '))
print(f'\033[1;30;41m{"<<<Programa Finalizado...":^36}')
