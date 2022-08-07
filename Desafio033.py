'''# Maior e menor valor
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
menor = n1
# Verificando menor valor
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando maior valor
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O menor valor digitado é {menor}! ')
print(f'O maior valor digitado é {maior}!')'''

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
lista = [a , b , c]
print('O menor valor digitado é: {}'.format(min(lista)))
print('O maior valor digitado é {}'.format(max(lista)))
