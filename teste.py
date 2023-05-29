'''def calcular_variancia(valores):
    media = sum(valores) / len(valores)
    soma_quadrados = sum((x - media) ** 2 for x in valores)
    variancia = soma_quadrados / (len(valores) - 1)
    return variancia



lista = 10, 2, 15, 11, 9, 3, 7, 15, 12, 5, 8
print(calcular_variancia(lista))'''

import numpy as np

x = np.array([5, 8, 7, 10, 6, 7, 9, 3, 8, 2])
y = np.array([6, 9, 8, 10, 5, 7, 8, 4, 6, 2])

cr = np.corrcoef(x, y)
corr = cr[0, 1]
print(cr)