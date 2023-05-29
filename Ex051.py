# Desenvolva um programa que leia o primeiro termo de uma PA.
# No final, mostre os 10 primeiros termos dessa prograessão.
print(f"{'='*30}\n10 Primeiros termos de uma PA\n{'='*30}")
p = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
d = p + (10 - 1) * r
for c in range(p, d + r, r):
    print(c, end='→ ')
print('Fim')
