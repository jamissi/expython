#Desenvolva um programa que leia seis números inteiros e
#Mostre a soma apenas daqueles que forem pares. Se o valor
#Digitado for impar, desconsidere-o.
soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'Você informou {cont} pares e a soma deles foi {soma}.')


