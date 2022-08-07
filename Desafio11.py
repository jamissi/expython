'''Faca um programa que leia a largura e a altura
de uma parede em metros, calcule a sua area e a quantidade de tinta
necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma
area de 2m2'''

l = float(input('Digite a largura da parede:'))
a = float(input('Digite a altura da parede:'))
la = l * a
print(f'A area da parede a ser pintada e: {la}')
p = la / 2
print(f'A quantidade de tinta a ser usada e: {p}')
