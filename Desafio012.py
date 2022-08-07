'''Faca um algoritmo que leia o preco de um
produto e mostre seu novo preco, com 5% de desconto.'''

n = float(input('Digite o valor do produto:'))
d = n - (n * 0.05)
print('O valor do produto com desconto:{:.1f}'.format(d))