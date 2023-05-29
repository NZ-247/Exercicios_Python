# Dentro do pacote utilidadesCev que criamos no desafio 111
# temos um módulo chamado dado
# Crie uma função chamada leiadinheiro() que seja capaz de funcinar como
# a função input(), mas com uma validação de dados
# Para aceitar apenas valores sejam monetários.
from Ex112.utilidadesCEV import dado, moeda
c = dado.leiaDin('Informe um valor R$: ')
moeda.resumo(c, 6, 9)
