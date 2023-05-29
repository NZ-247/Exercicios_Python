# Crie um programa que leia a idade e o sexo de várias pessoas
# A cada pessoa cadastrada, o programa deverá perguntar ao usuário se quer coninuar
# No Final Mostre:
# A) Quantas pessoas tem mais de 18 anos.

# B) Quantos Homens foram cadastrados.

# C) Quantas Mulheres tem menos de 20 anos.
print(f'{"Banco de Dados":=^40}')
print(f'{"-"*40}\nCadastro de Clientes\n{"-"*40}')
mais18 = h = m20 = 0


while True:
   sexo = ' '
   while sexo not in 'MF':
      sexo = str(input('Sexo [M/F]: ')).upper().strip()
   idade = int(input('Idade: '))
   if sexo == 'F' and idade <= 20:
         m20 += 1
   else:
      h += 1
   if idade > 18:
      mais18 += 1
   if sexo == 'M':
      h += 1
   parar = ' '
   while parar not in 'SN':
      parar = str(input('Deseja Adicinar mais Dados? [S/N]')).upper().strip()
   if parar == 'N':
      break
print(f'Programa finalizado!\nsegundo os dados {h} das pessoas cadastradas são Homens\nHá {mais18} pessoas com mais de 18 anos\nE {m20} Mulheres tem mais de 20 anos.')
