# Faça um programa chamada escreva()
# Receba o texto e mostre uma mensagem com tamanho adaptável.
def escreva(txt):
    print(f'{"="*(len(txt)+4)}\n  {txt}\n{"="*(len(txt)+4)}')


frase = str(input('Digite algo: '))
escreva(frase)
