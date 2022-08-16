'''Escreve um programa que leia um valor em metros e o
exiba em centimentos e milimetros'''

m = float(input('Digite o valor em metros: '))
c = m * 100
mm = m * 1000
print(f'Centimentros = \033[1;35;41m{c}\033[m \nMilimetros = \033[1;32m{mm}\033[m')
