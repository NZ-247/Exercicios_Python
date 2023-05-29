# Adapte o código do desafio 107, criando uma função adcional chamada moeda()
# que consiga mostrar os valores como um formato monetário
from Ex108met import moeda

p = int(input('Digite um valor: '))
t = int(int(input('Quanto Será taxa (%) de aumento? ')))
d = int(input('Qual a porcentagem de declínio? '))
print(f'O dobro do valor {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}\n'
      f'Com aumento de {t}% passa a veler {moeda.moeda(moeda.aumento(p, t))}\n'
      f'Diminuindo {d}% de {moeda.moeda(p)} temos {moeda.moeda(moeda.diminuir(p, d))}\n'
      f'A Metade de {moeda.moeda(p)} equivale a {moeda.moeda(moeda.metade(p))}')
