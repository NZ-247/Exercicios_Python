# escreva um programa que pergunte o salário de um funcionário e caulcule o seu aumento.
# Para salários superiores à R$:1250, caulcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%.
s = float(input('Digite o salário do funcionário para calcular o seu aumento: R$'))
if s >= 1250:
   s = s + (s*0.1)
else:
    s = s + (s*0.15)
print(f'O novo Salário deste funcionário será {s}.')
