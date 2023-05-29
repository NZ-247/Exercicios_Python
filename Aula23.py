# Tratamento de Erros e Exeções
try:
    a = int(input('Numerador:'))
    b = float(input('Denominador:'))
    s = a / b
except ZeroDivisionError:
    print('Não é possessive dividir um número por Zero')
except (TypeError, ValueError):
    print(f'Houve Problemas com o tipo dos dados informados.')
except Exception as erro:
    print(f'A causa do erro foi {erro.__cause__}')
except KeyboardInterrupt:
    print('O usuário prefiriu não informar os dados.')
else:
    print(f'O Resultado é: {s}')
finally:
    print('volte Sempre! muito Obrigado!')
