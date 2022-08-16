'''Crie um programa que leia quanto dinheiro uma pessoa tem
na carteira e mostre quantos Dolares ela pode comprar.'''

n = float(input('Digite a quantidade em reais: R$'))
d = n / 3.27
print(f'Com R$\033[4;31m{n}\033[m é possível comprar $\033[4;36m{d}\033[m.')

col