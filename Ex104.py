# Crie uma função leiaint(), que vai funcionar d forma semelhante à função input()
# Só que a validação para apenas um valor numérico.


def leiaint(numero):
    while True:
        receba = input(f'{numero}')
        if receba.isnumeric():
           receba = float(receba)
           return receba
        else:
            print(f'\033[1;31mERRO! Digite um Número inteiro\033[m')


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')
