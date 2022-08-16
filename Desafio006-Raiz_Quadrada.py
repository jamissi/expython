'''Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada:'''

x = int(input('Escolha um numero:'))
d = x * 2
t = x * 3
r = x ** (1/2)
cor = {'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33m',
    'lilas':'\033[35m'}
print('O dobro = {}{}{} \nO triplo = {}{}{} \nA raiz quadrada = {}{}{}'.format(cor['azul'], d, cor['limpa'], cor['amarelo'], t, cor['limpa'], cor['lilas'], r, cor['limpa']))
