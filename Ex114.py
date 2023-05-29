# Crie um código em Python
# Que teste se o Site Pudim
# Está acessível pelo computation usado.
import urllib.request
import urllib
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')

except:
    print('\033[1;33mO site informado não está disponível!\033[m')

else:
    print('\033[1;34mO Site está disponívrl na web!')
