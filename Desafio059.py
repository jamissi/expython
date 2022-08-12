from time import sleep
x = float(input('Digite o 1° valor: '))
y = float(input('Digite o 2° valor: '))
op = 0
while op != 5:
    print('''\nEscolha uma opção: 
     [1] SOMAR
     [2] MULTIPLICAR
     [3] MAIOR
     [4] NOVOS NÚMEROS
     [5] SAIR DO PROGRAMA''')
    op = int(input('\nOpção: '))
    #SOMA
    if op == 1:
        print('-' * 22)
        soma = x + y
        print('A soma dos valores:')
        print(f'{x} + {y} = {soma}')
        print('-' * 22)
    #MULTIPLICAÇÃO
    elif op == 2:
        mul = x * y
        print('-' * 22)
        print('Os valores multiplicados: ')
        print(f'{x} * {y} = {mul}')
        print('-' * 22)
    #MAIOR
    elif op == 3:
        if x > y:
            print('-' * 22)
            print(f'O {x} é maior que {y}.')
        else:
            print('-' * 22)
            print(f'O {y} é maior que {x}.')
        print('-' * 22)
    #NÚMEROS NOVOS
    elif op == 4:
        x = float(input('Digite o 1° valor: '))
        y = float(input('Digite o 2° valor: '))
    #FINALIZANDO
    elif op == 5:
        print('Finalizando...')
    #OPCAO INVALIDA
    else:
        print('\nOpção inválida.')
    sleep(1)
print('FIM')

