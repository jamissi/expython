'''Refaça o desafio 035 dos triângulos,
acrescentando o recurso de mostrar que tipo de triângulo será formado:
-Equilátero: todos os lados iguais
-Isósceles: dois lados iguais
-Escaleno: todos os lados diferentes'''

a = float(input('\n\033[1mPrimeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))
if a + b > c and b + c > a and a + c > b:
    print('\n\033[1mÉ possivel criar um triângulo e ele será:')
    if a == b == c:
        print('\033[1;34mEquilátero.')
    elif a == c or a == b or b == c:
        print('\033[1;33mIsósceles.')
    elif a != b or a != c or b != c:
        print('\033[1;35mEscaleno.')
else:
    print('\n\033[1;31;43mNão é possivel formar um triângulo com essas medidas.\033[m')
