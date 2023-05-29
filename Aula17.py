#clientes = [['nathy', 19], ['Anny', 18], ['David', 19], ['Matheus F', 18], ['Gotarde', 19], ['Jeffs', 20]]
#for p in clientes:
#    print(f'\033[4;33m{p[0]}\033[m tem \033[36m{p[1]}\033[m Anos de Idade.')
pov = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pov.append(dado[:])
    dado.clear()
print(pov)
