from Ex107 import úteis

num = int(input('Digite um Número: '))
expo = int(input('Informe um expoente: '))
fat = úteis.factory(num)
print(f'O fatorial de {num} é {fat}.\n'
      f'O Dobro vale {úteis.dobro(num)}.\n'
      f'O triplo é igual á {úteis.triplo(num)}.\n'
      f'O Produto da exponencição equivale à {úteis.potencia(num, expo)}')
