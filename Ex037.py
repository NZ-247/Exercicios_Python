# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher a base de conversão.
# -1 para binário
# -2 para octal
# -3 para hexadecimal
n = int(input('Digite um Número \033[4;34minteiro\033[m: '))
print('''Escolha um base para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para EXADÉCIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{n} Convertido para BINÁRIO é igual à {bin(n)[2:]}')
elif opção == 2:
    print(f'{n} Convertido para OCTAL é igual à {oct(n)[2:]}')
elif opção == 3:
    print(f'{n} Convertido para HEXADÉCIMAL é igual à {hex(n)[2:]}')
else:
    print('Opção \033[4;33minválida\033[m, selecine uma das três acima!')
