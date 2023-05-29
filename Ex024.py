# faça um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Novo".
n = str(input('Qual é o \033[4;33mnome\033[m da \033[1;36mcidade\033[m onde você mora? ')).strip().upper()

print(n[:4] == 'NOVO')
