#Faça um programa que mostre na tela
#uma contagem regressiva para o estouro
#de fogos de artifiício, indo de 10 até 0,
#com uma pausa de 1 segundo entre eles

from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
    print('-*-' *2)
print('*-*-* FELIZ ANO NOVO!! *-*-*')
