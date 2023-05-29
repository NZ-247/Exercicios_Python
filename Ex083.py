# Crie um Programa onde o usuário digite uma expressão qualquer que use parênteses
# Sua aplicação deverá analisar se a expressão passada está com os parêteses abertos e fechados na ordem certa.
sb = []
expressao = (str(input('Escreva uma Expressão: ')))
for sim in expressao:
    if sim == "(":
        sb.append('(')
    elif sim == ')':
        if len(sb) > 0:
            sb.pop()
        else:
            sb.append(')')
            break
if len(sb) == 0:
    print('Exprassão Válida!')
else:
    print('Expressão Inválida!')
