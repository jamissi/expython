#Crie um programa que leia
#o ano de nascimento de sete pessoas
#No final, mostre quantas pessoas ainda
#não atingiram a maioridade e quantas já são maiores - 21 anos
from datetime import date
menores = 0
maior = 0
print('Digite o ano de nascimento', )
for c in range (1,8):
    ano = int(input(f' {c}º pessoa: '))
    if date.today().year - ano < 21:
        menores += 1
    else:
        maior += 1
print(f'Existem {maior} maiores de idade e {menores} menores. ')
