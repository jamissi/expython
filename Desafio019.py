# Um professor quer sortear um dos seus quatros alunos pra apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
Aluno1 = input('Primeiro aluno: ')
Aluno2 = input('Segundo aluno: ')
Aluno3 = input('Terceiro aluno: ')
Aluno4 = input('Quarto aluno: ')
Lista = [Aluno1, Aluno2, Aluno3, Aluno4]
escolhido = choice(Lista)
print(f'O aluno escolhido foi {escolhido}!')