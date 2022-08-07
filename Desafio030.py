n = int(input('Escolha um número para saber se ele é par ou ímpar: '))
r = n % 2
if r == 0:
    print(f'O número {n} é par!')
else:
    print(f'O número {n} é ímpar!')