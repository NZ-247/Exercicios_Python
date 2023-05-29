# faça um programa que leia uma frase pelo teclado que mostre:
# Quantas vezes uma letra se repete
# em que posição aparece a primeira
# Em que posição aparece a última.
f = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra "A" aparece {f.count("A")} vezes na frase.\nSendo a primeira na posição {f.find("A")+1}.\nE a última na {f.rfind("A")+1}')
