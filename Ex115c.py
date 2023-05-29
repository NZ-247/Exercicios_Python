from Ex115met import sisNZ
from Ex115met.arquivo import *

nomes = []
idade = []
p = 0
arq = 'dados.txt'

if not filex(arq):
    criarArq(arq)

while p < 1:
    try:
        while True:
            print(f'{"NZsql":=^36}')
            op = int(input(f'''        \033[33m[1] - \033[34mNovo cadastro
        \033[33m[2] - \033[34mListar cadastros
        \033[33m[3] - \033[34mSair\033[32m
            {"--" * 18}
             Opção: \033[m '''))

            if op == 1:
                n = sisNZ.nameValid()
                i = sisNZ.idValid()

                sisNZ.cadastrar(arq, n, i)
            elif op == 2:
                '''if len(n) == 0:
                    print('Não há nada à mostrar :(...')
                else:
                    lerArquivo(arq)'''
                try:
                    lerArquivo(arq)
                except Exception as erro:
                    print(f"não foi passível ler o arquivo{erro}")


            elif op == 3:
                p = 3
                break
            else:
                print(f'\033[1;31mErro!!!\033[4;33m Opção inválida!\033[m')
        print(f'\033[1;34mMuito Obrigado!\033[36m Volte Sempre...;)\033[m')
    except ValueError:
        print("Opção inválida! Digite apenas 1, 2 ou 3...")
