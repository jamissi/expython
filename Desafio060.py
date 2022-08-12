from time import sleep
numero = int(input('Digite um numero: '))

contador = numero
f = 1

print(f'Calculando {numero}! -> ', end='')

sleep(1)

while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    f *= contador
    contador -= 1
print(f'{f}')
