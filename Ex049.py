# Refaça o Desafio 009, mostrando a tabuada de um número que o user escolheu
# Só que agora faça utilizando laço For
n = int(input('Digite um número e veja sua tabuáda: '))
print(f'{"-"*20}\nTabuada do {n}')
for c in range(0, 11):
    print(f'{n} x {c} = {c*n}')
print('-'*20)
