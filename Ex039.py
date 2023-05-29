from datetime import date
a = date.today().year
i = int(input('Em que ano você nasceu? '))
if a - i == 18:
    print(f'Você deve se alistar Imediatamente!')
elif a - i > 18:
    print(f'Huuuuum {a - i} anos, Você já deve ter feito seu alistamento à {(a - i) - 18} anos então.')
    d = str(input('\033[33mNão é mesmo\033[m? (\033[1;37mResponda: S/N\033[m) ')).upper()
    if d == 'S':
        print('Há sim, Tudo certo então.')
    elif d == 'N':
        print('Mais deveria em amigão, isso é muito importante!.')
elif a - i < 18:
    print(f'Ainda é cedo, você tem só \033[4;33m{a - i}\033[m anos, Mas Lembre-se de fazer seu alistamento em {(18 - (a - i)) + a}.')
