# A federação de natação preisa de um programa que leia o ano de nascimento de um atlata e mostre sua categoria:
# - até 9 anos: mirim
# - até 14 anos: infantil
# - até 19 anos: júnior
# - até 25 anos: sênior
# acima : Master
i = int(input('Digite sua idade e veja sua categoria: '))
if i <= 9:
    print('Sua Categoria é \033[4;34mMirim\033[m.')
elif i < 14:
    print('Sua categoria é \033[4;32mInfantil\033[m.')
elif i < 19:
    print('Sua categoria é \033[4;36mJúnior\033[m.')
elif i < 25:
    print('Sua categoria é \033[4;35mSênior\033[m')
else:
    print('Sua categoria é \033[4;31mMaster\033[m')
