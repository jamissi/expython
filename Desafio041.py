'''Faça um programa que leia o ano de nascimento de um atleta e mostra
sua categoria, de acordo com a idade:
-Até 9 anos: Mirim
-Até 14 anos: Infantil
-Até 19 anos: Junior
-Até 20 Anos: Sênior
-Acima: Master'''


from datetime import date
atual = date.today().year
ano = int(input('ANO DE NASCIMENTO: '))
idade = atual - ano
print(f'A idade do atleta, {idade}.')
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <=19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')