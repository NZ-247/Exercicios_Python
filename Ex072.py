# Crie um Programa que tenha uma tupla totalmente preencida com uma contagem por extenso, de Zero à vinte
# Seu Programa deverá ler um número pelo teclado (entre 0 - 20) e mostrá-lo por extenso.
numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
           'Cinco', 'Seis', 'Sete', 'Oito',
           'Nove', 'Dez', 'Onze', 'Doze',
           'Treze', 'Quatorze', 'Quinze', 'Dezesseis',
           'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    r = int(input('Digite um valor DE 0 à 20: '))
    if 0 > r or r > 20:
        print('Resposta Inválida! Tente Novamente.')
    else:
        break
print(f'Você digitou o Número: {numeros[r]}')
