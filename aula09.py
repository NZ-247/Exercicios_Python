# Aula 09-Manipulando texto
frase = '\033[4;33m Aula 09 do curso de python\033[m'
print(frase)
print(f'{frase[8]}\n{frase[19]}\n{frase[19:27]} \033[7;33{frase[26:]}')
print(f'{frase.count("o")}')
print(f'{frase.replace("python", "Andriod")}')
print('curso' in frase)
div = frase.split()
print(div[6])
print(div[6][3])