# faça um programa que leia o nome de um usuário e se ele tem determinado sobrenome.
n = str(input('Digite \033[1;33mseu\033[m nome \033[4;34mcompleto\033[m: ')).strip().upper()
print('SILVA' in n)
