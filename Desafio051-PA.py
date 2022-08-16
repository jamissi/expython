#Desenvolva um programa que leia
#o primeiro termo e a razão de uma PA.
#no final, mostre os 10 primeiros termos
#dessa progressão.

a1 = int(input('Digite o primeiro elemento da progressão: '))
ra = int(input('Digite a razão da progressão: '))
dec = a1 + (10 -1)*ra
for va in range(a1, dec + ra, ra):
    print(va, end=' -> ')
print('Fim')