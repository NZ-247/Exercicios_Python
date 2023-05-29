def dobro(preco):
    d = preco * 2
    return d


def triplo(preco):
    t = preco * 3
    return t


def aumento(preco, taxa):
    preco += preco * (taxa/100)
    return preco


def diminuir(preco, taxa):
    preco -= preco * (taxa/100)
    return preco


def metade(preco):
    return preco/2



