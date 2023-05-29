# Crie um programa que tenha as funções incorporadas:
# aumentar(), diminuir(), dobro() e metade()
# faça também um programa que importe esse módulo e use  algumas dessa funções.
import moeda

print(f'\n{"="*36}\n{"Calculadora":^36}\n{"="*36}')
num = int(input('Digite um valor: '))
au = int(input('Quantos Porcento (%) quer de aumento desse valor? '))
dim = int(input('E Quanto quer diminuir dele? '))
print(f'\n{"---"*36}\nO valor digitado foi {num}\nCom aumento de {au}% fica com valor igual a {moeda.aumento(num, au)}\n'
      f'Com redução de {dim}% passa a valer {moeda.diminuir(num, dim)}'
      f'\nO dobro vale {moeda.dobro(num)}\nE a sua metade vale {moeda.metade(num)}')
