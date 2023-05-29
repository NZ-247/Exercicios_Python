# Refaça o Desafio 051, lendo o primeiro termo e a razão de uma PA.
# Mostrando os 10 primeiros termos das progreçâo usando a estrutura While.
print(f'{"Gerador de PA 2.0":=^20}')
t1 = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
t = 1
while t <= 10:
    print(t1, ' → ', end=' ')
    t1 += r
    t += 1
print('Fim')
