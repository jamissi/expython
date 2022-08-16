'''Desenvolva um programa que leia as duas notas de um aluno, calcule e mostra a sua media: '''

n1 = float(input('Digite a nota um: '))
n2 = float(input('Digite a nota dois: '))
m = (n1 + n2) / 2
if m < 5:
    cor = {'l':'\033[m',
       'r':'\033[1;31m'}
    print("A média = {}{}{}".format(cor['r'], m, cor['l']))
else:
    cor = {'l': '\033[m',
           'b': '\033[1;34m'}
    print("A média = {}{}{}".format(cor['b'], m, cor['l']))


