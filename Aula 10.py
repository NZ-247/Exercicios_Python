# condiçoes simples e composta.
n1 = float(input('Digite a nota do seu primeiro bimestre: '))
n2 = float(input('Digite a nota do seu segundo bimestre: '))
n = (n1+n2)/2
if n >= 60.0:
    print(f'Você está \033[4;32maprovado!\033[m Sua Média foi {n:.1f}.')
else:
    print(f'\033[4;33mREPROVADO!\033[m,pois {n:.1f} é abaixo da média necessária, se dedique mais no próximo ano.')
