# Melhore o desafio 061
# perguntando para o usuário se ele quer mostrar mais termos.
# O programa enocerra quando ele disser que quer mostrar 0 termos.
print(f'{"Gerador de PA 3.0":=^40}')
p = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
q = 0
t = int(input('Quantia de termos da PA: '))
while t > 0:
    print(p, ' → ', end='')
    p += r
    t -= 1
    if t == 0:
        o = int(input('Quantos Termos à mais quer exibir? '))
        t = o
    q += 1
print(f'Foram Exibidos um total de {q} Termos da PA.')
