def leiaDin(msg):
    ok = False
    while not ok:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == ':':
            print(f'\033[4;31mERRO!\033[m \"{entrada}\" \033[0;33mNão é um número!\033[m')
        else:
            ok = True
            return float(entrada)


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
