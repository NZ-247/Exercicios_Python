# Crie uma função chamada voto que receba com parâmetro o ano de nascimento de uma pessoa
# Retornado um valor literal indicando se uma pessoa tem voto negado opcinal ou obrigatório


def voto(data):
    from datetime import date
    i = date.today().year - data
    print(f'Com \033[1;36m{i}\033[m anos o Voto', end='')
    if i < 18:
        return ' \033[1;32mNão vota ainda!\033[m'
    elif 16 <= i < 18 or i > 60:
        return ' é \033[1;24mOpcinal!\033[m'
    else:
        return ' é \033[4;33mobrigatório!\033[m'


p = int(input('Digite seu ano de nascimento: '))
print(f'{voto(p)}')
