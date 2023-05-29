# Adicione ao módulo moeda.py uma função chamada resumo()
# Que mostre na tela algumas informações geradas pelas funções
# Que já temos criado até aqui.
from moedas import resumo
v = int(input('Insira um valor: '))
a = int(input('Taxa de acréscimo: '))
d = int(input('Taxa de Declíneo: '))
resumo(v, a, d)
