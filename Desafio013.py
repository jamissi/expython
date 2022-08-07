'''Faca um algoritmo que leia o salario de um funcionario
e mostre seu novo salario com 15% de aumento'''

n = float(input('Digite seu salario sem o aumento:'))
au = n + (n * 0.15)
print('O salario com o aumento e: {:.1f}'.format(au))