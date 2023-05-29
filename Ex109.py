# Modifique as funções criadas no desafio 107 para que aceitem
# um parâmetro à mais, informando se o valor retornado
# vai ou não ser formatado pela função moeda()
# desenvolvida no desafio 108.
from Ex109met import moeda

p = int(input('Digite um valor: '))
au = int(input('Quantos porcento (%) terá de aumento? '))
dim = int(input('Quantos porcento (%) será a redução? '))
print(f'A metade de {p} é {moeda.metade(p)}\nO Dobro vale {moeda.dobro(p, True)}\n'
      f'Com aumento de {au}% passa à ser {moeda.aumento(p, au, True)}\n'
      f'Diminuindo {dim}% valor é igual a {moeda.diminuir(p, au, True)}')
