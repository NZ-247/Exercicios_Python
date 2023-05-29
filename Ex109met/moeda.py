def dobro(preco=0, formato=False):
    d = preco * 2
    return d if formato is False else moeda(d)


def triplo(preco=0, formato=False):
    t = preco * 3
    return t if not formato else moeda(t)


def aumento(preco=0, taxa=0, formato=False):
    preco += preco * (taxa/100)
    return preco if formato is False else moeda(preco)


def diminuir(preco=0, taxa=0, formato=False):
    preco -= preco * (taxa/100)
    return preco if not formato else moeda(preco)


def metade(preco, formato=False):
    p = preco/2
    return p if formato is False else moeda(p)


def moeda(valor=0, moeda='R$:'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')




