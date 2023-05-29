def ler_int(inteiro):
    while True:
        try:
            numero = int(input(inteiro))
        except ValueError:
            print('Houve um problema, essa função lê apenas números inteiros!')
        else:
            return numero


def ler_float(racional):
    while True:
        try:
            numero = float(input(racional))
            if numero.is_integer():
                raise ValueError('Esse é valor é inteiro! Digite um número Real válido!')
            return numero
        except ValueError as erro:
            print(f'\033[4;31mErro!\033[0;33m Causa do Erro:\033[m {erro}')
