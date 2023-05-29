# crie um programa que leia uma frase qualquer
# E diga se ela é um palíndromo, Descondiferando os espaços.
f = str(input('Digite uma frase: ')).upper().replace(' ', '')
fi = f[::-1]
if f == fi:
    print(f'A frase "{f}" é um Palíndromo.')
else:
    print(f'A frase "{f} não um palíndromo.')
