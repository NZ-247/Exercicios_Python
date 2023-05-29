def dobro(preco=0):
    d = preco * 2
    return d


def triplo(preco=0):
    t = preco * 3
    return t


def aumento(preco=0, taxa=0):
    preco += preco * (taxa/100)
    return preco


def diminuir(preco=0, taxa=0):
    preco -= preco * (taxa/100)
    return preco


def metade(preco=0):
    return preco/2


def moeda(valor=0, moeda='R$:'):
    return f'{moeda}{valor}'.replace('.', ',')
