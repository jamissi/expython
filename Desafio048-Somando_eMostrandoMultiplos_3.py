# faça um programa que calcule a soma entre todos
# os números impares que são mútliplos de 3
# e que se encontram no intervalo de 1 até 500

cont = 0 #contador +1
s = 0 #acumulador +x
for c in range(3, 501, 6):
    if c % 3 == 0 and c % 2 == 1:
        cont = cont + 1
        s += c
        print(c)
print(f'A soma dos {cont} números é {s}')
