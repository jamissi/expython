'''Escreva um programa que leia dois números inteiros e compare-os,
mostrando na tela uma mensagem:
 -O primeiro valor é maior - O segundo valor é maior - Os valores são iguais.'''

print('\033[1mEscolha dois números inteiros.')
n = int(input('Digite aqui o primeiro valor: '))
n2 = int(input('Digite aqui o segundo valor: \033[m'))
if n > n2:
    print('\033[1mO primeiro valor escolhido é \033[1;31;40mMAIOR\033[m\033[1m que o segundo.')
elif n < n2:
    print('primeiro valor escolhido é \033[1;35;40mMENOR\033[m \033[1mque o segundo.')
else:
    print('\033[1mOs valores digitados são \033[1;33;40mIGUAIS\033[m.')