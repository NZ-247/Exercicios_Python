# Desenvolva um programa que leia quatro valores pelo teclado e armazene numa Tupla
# A) Quantas vezes apareceu o valor 9
# B) Em que posição foi digitado o primeiro valor 3
# C) Quais Foram os números pares.
nums = ()
for c in range(0, 5):
    num = int(input('Digite um número: '))
    nums += (num,)

print(f'Os valores digitados foram:\n {nums}\nO número 9 foi digitado {nums.count(9)} vezes.')
if 3 in nums:
    print(f'O 3 foi digitado na possição {nums.index(3) + 1}')
else:
    print('O valor 3 não foi digitado.')
print(f'Dos Numeros digitados os pares são: ')
for n in nums:
    if n % 2 == 0:
        print(n, end=' ')
