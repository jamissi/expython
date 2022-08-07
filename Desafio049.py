#Refaça o desafio 009, mostrando a tabuada  de um número
#que o usuário escolher, só que agora utilizando o laço FOR.
n = int(input('Digite um número para saber a tabuada dele: '))
for c in range(0, 11):
    s = n * c
    print(s)

#Guanabara
x = int(input('Digite um número para saber a sua tabuada: '))
for y in range(0, 11):
    print('{} x {:2} = {}'.format(x, y, x * y))
