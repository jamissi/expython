'''Faca um programa que leia um numero inteiro e mostre na tela seu sucessor e seu antecessor:'''

x = int(input('Digite um numero: '))
su = x + 1
an = x - 1
print('O sucessor é {}{}{} \nE seu antecessor é {}{}{}'.format('\033[1;36m', su, '\033[m', '\033[1;34m', an, '\033[m'))
