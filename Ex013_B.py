p = float(input('Qual o \033[1;32mvalor\033[m do produto?R$:'))
por = float(input('De quantos % será o \033[1;32mdesconto\033[m à \033[1;36mvista\033[m? '))
pra = float(input('De quantos % será o \033[1;31maumento\033[m à \033[1;33mprazo\033[m? '))
print(f'O produto à \033[1;36mvista\033[m tem \033[1;33m{por}\033[m% de \033[1;32mdesconto\033[m, com isso o preço vai  de R$:\033[1;31m{p}\033[m para R$:\033[1;32m{p-por*p/100}\033[m\njá à \033[4;33mprazo\033[m terá um \033[1;31maumento\033[m de \033[4;36m{pra}\033[m% , passando a custar R$:\033[1;31m{p+p*pra/100}\033[m')
