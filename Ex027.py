# fsça um progrsms que leia o nome completo do usuário .
# mostrando separadamente o primeiro eo ultimo nome.
n = str(input('Digite o seu nome \033[4;35mcompleto\033[m: ')).strip()
nome = n.split()
print(f'Olá, \033[1;36m{nome[0]}\033[m é bom ter voçe comigo nesse programa \033[1;33m:)\033[m\nPude perceber que seu primeiro nome é \033[1;34m{nome[0].capitalize()}\033[m\nE Seu \033[4;31múltimo\033[m nome é \033[4;35m{nome[len(nome)-1]}\033[m')
