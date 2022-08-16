menu = 0
cont = 0
soma = 0
menu = int(input('Digite um número (999 P/ SAIR): ')) #PARA NÃO FAZER A CONTAGEM DO 999

while menu != 999:
    cont += 1
    soma += menu
    menu = int(input('Digite um número (999 P/ SAIR): ')) #PARA NÃO FAZER A CONTAGEM DO 999

print(f'Você digitou {cont} e a soma deles foram {soma}')

