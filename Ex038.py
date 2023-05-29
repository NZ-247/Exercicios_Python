# Escreva programa que leia um programa que leia dois números inteiros e compare-os, mostrando na tela um mensagem.
# - O primeiro valor é maior.
# - O segundo valor é maior.
# - Não tem valor maior, os dois são iguais.
v1 = int(input('Digite um \033[4;34mnúmero\033[m: '))
v2 = int(input('\033[1;34mDigite \033[4;33moutro\033[m: '))
if v1 > v2:
    print('O \033[1;36mprimeiro\033[m número Digitado é \033[4;31mmaior\033[m.')
elif v1 < v2:
    print('O \033[1;35mSegundo\033[m Número é \033[1;31mmaior\033[m')
else:
    print('\033[1;31mNão\033[m tem \033[4;37mMaior\033[m, os dois São \033[4;36miguais\033[m.')
