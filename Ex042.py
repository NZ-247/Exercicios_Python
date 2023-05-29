# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: Todos os lados iguais
# - isósceles: Dois lados iguais
# - Escaleno: Todos os lados diferentes...
print('Digite três medidas e veja se é possível fomar um triângulo com elas:')
m1 = float(input('medida 1: '))
m2 = float(input('medida 2:'))
m3 = float(input('Medida 3: '))
if (m1 + m2) > m3 and (m1 + m3) > m2 and (m2 + m3) > m1:
    print('É possível formar um triângulo ', end='')
    if m1 == m2 == m3:
        print('Equilátero.')
    elif m1 != m2 != m3 != m1:
        print('Isósceles')
    else:
        print('Escaleno')
        