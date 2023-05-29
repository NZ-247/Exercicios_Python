# Funções (Parte 1).
# Criando funções simples:
def lin():
    print('\033[1;36m-\033[m'*36)


lin()
print('Curso em Vídeo')
lin()


# Funções com parâmetros:
def titulo(msg):
    print(f'{"-"*20}\n{msg}\n{"-"*20}')


titulo('Aprenda Python')
titulo('Programa em Python')
titulo('Python é Show')


# Funçõs com parâmetros listas:
def dobra(lst):
    pos = 0
    inc = lst[:]
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(f'O Dobro de {inc} é {lst} ')


valores = [2, 4, 6, 8]
dobra(valores)


# Funções com parâmetros variáveis (desempacotamento de parâmetros)
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(2, 5, 98)
