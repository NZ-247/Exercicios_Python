# crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quamtos já são maiores.
from datetime import date
tm = 0
tn = 0
for c in range(7):
    na = int(input(f'Ano de nascimento da {c+1}° pessoa: '))
    i = date.today().year - na
    print(i)
    if i > 21:
        tm += 1
    else:
        tn += 1
print(f'De acordo com os dados informadas, há {tm} pessoas que possuem a maior idade.\nDo Mesmo modo há, {tn} que não atingiram ainda.')
