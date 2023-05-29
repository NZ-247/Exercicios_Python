import random

n = random.randint(1, 10)
print(n)
no = input("Qual é o seu nome? ")
import emoji

print(emoji.emojize(f"Eae \033[4;33m{no}\033[m :thumbs_up:"))
