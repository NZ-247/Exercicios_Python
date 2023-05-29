n = str(input('\033[1;34mDigite\033[m \033[4;35mseu\033[m \033[1;33mNome\033[m: '))
print(f'Bom Dia \033[1;36;40m{n}\033[m!')
if n == 'Alan':
    print('Que Belo nome amigo')
elif n == 'pedro' or n == 'maria' or n == 'João':
    print('Seu nome é bem comum no Brasil.')
elif n == 'José' or 'Matheus' or 'Tiago' or 'Paulo':
    print('Seu nome é Bíblico, que Bacana.')
else:
    print('Gostei do seu nome.')
print('Tenha um ótimo \033[4;33mdia\033[m.')
