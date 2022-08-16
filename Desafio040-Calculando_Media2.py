'''Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
-Média abaixo de 5.0 = Reprovado
-Média entre 5.0 e 6.9 = Recuperação
-Média 7.0 ou superior = Aprovado'''

nota1 = float(input('Boa tarde, digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2 ) / 2
if media < 5.0:
    print(f'A média do aluno foi \033[1;31m{media}\033[m. '
          f'\nO aluno foi \33[1;31mreprovado\033[m!')
elif media <= 6.9:
    print(f'A média do aluno foi \033[1;32m{media}\033[m. '
          f'\nO aluno ficou de \033[1;32mrecuperação\033[m!')
else:
    print(f'A média do aluno foi \033[1:34m{media}\033[m. '
          f'\nO aluno foi \033[1;34maprovado\033[m!')