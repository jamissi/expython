#FAÇA UM PROGRAMA QUE LEIA
#UM NÚMERO INTEIRO E DIGA
#SE ELE É OU NÃO UM NÚMERO PRIMO
tot = 0
n = int(input('Digite um número: '))
for c in range(1, n +1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO numero {n} foi divisivel {tot} vezes!' )
if tot == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo!')