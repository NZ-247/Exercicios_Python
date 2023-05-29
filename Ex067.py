# Faça um Programa que mostre a tabuada de vários números
# um de cada vez, para cada valor digitado pelo usuário
# O Progrss será Interrompido quando o valor solicitado for negativo.
print(f'{"Tabuada V3.6":=^37}')
while True:
    print('-'*37)
    n = int(input('Digite um  número e veja sua tabuada: '))
    if n < 0:
        break
# print(f'''Tabuada do {n}:
#{n} X  1 =  {n}
#{n} X  2 =  {n*2}
#{n} X  3 =  {n*3}
#{n} X  4 =  {n*4}
#{n} X  5 =  {n*5}
#{n} X  6 =  {n*6}
#{n} X  7 =  {n*7}
#{n} X  8 =  {n*8}
#{n} X  9 =  {n*9}
#{n} X 10 =  {n*10}''')
#print('Programa finalizado! Até a Próxima.')''''''
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}')
print('Programa Finalizado! Até a Próxima.')