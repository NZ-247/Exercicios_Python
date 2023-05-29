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


def resumo(valor, taxa=0, reducao=0):
    from moedas import aumento, diminuir, dobro, metade, moeda, triplo
    print(f'\033[4;33m{" "*36}\n{"RESUMO DE VALORES":^36}\033[m\n'
          f'{"Preço analisado:":-<20}{moeda(valor):->16}\n'
          f'{"Dobro Do Preço:":-<20}{dobro(valor, formato=True):->16}\n'
          f'{"Metade do Preço:":-<20}{metade(valor, formato=True):->16}\n'
          f'{f"{taxa}% de aumento:":-<20}{aumento(valor, taxa, formato=True):->16}\n'
          f'{f"{reducao}% de Redução:":-<20}{diminuir(valor, reducao, formato=True):->16}\n'
          f'{f"Triplo de {valor}:":-<20}{triplo(valor, formato=True):->16}')
