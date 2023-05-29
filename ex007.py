n1 = float(input('Qual foi a nota do seu primeiro bimestre? '))
n2 = float(input('E a do segundo? '))
#print(f'A Média aritimética das sua notas é {(n1+n2)/2}')
if (n1+n2)/2 <= 60:
    print(f'A \033[1;33mMédia\033[m aritimédica das suas notas é \033[1;31m{(n1+n2)/2:.1f}\033[m.')
else:
    print(f'A \033[1;33mMédia\033[m aritimédica de suas notas é \033[1;32m{(n1+n2)/2:.1f}\033[m.')
