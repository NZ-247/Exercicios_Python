# Crie um programa que leia as notas de um aluno e diga se ele está aprovado, de recuperação ou reprovado.
# Méfia abaixo de 50.0:Reprovado
# Média entre 50.0 e 69.9:Recuperação
# Média 70.0 ou superior:aprovado
print('Digite as notas dos seus 4 bimestres:')
n1 = float(input('1°- '))
n2 = float(input('2°- '))
n3 = float(input('3°- '))
n4 = float(input('4°- '))
m = (n1+n2+n3+n4)/4
if m >= 70.0:
    print('\033[4;36mAprovado\033[34m!\033[m')
elif m >= 50.0 and m < 70.0:
    print('Você não passou, mas também não Reprovou Ainda, está de \033[4;33mRecuperção\033[31m!\033[m')
else:
    print(f'\033[31mReprovado\033[33m!\033[m')
print(f'Sua Média foi {m}')
