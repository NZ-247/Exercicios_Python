#Aula 008 Conversor de Medidas
v = float(input('Digite o valor de uma medida em \033[4mMetros\033[m: '))
print(f'\033[1;33m{v}\033[m metros é igual à ', v*1000, 'mm')
print(f'\033[1;33m{v}\033[m metros = {v*100}  cm')
print(f'\033[1;33m{v}\033[m Metros = {v*10}   dc')
print(f'\033[1;33m{v}\033[m Metros = {v/10}   dam')
print(f'\033[1;33m{v}\033[m Metros = {v/100}  hm')
print(f'\033[1;33m{v}\033[m Metros = {v/1000} km')
