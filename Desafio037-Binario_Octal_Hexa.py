'''Escreva um programa que leia um número inteira qualquer
e peça para o úsuario escolher qual será a base de conversão:
1 para Binário; 2 para Octal; 3 para Hexadecimal.'''

num = int(input('Dgite um número inteiro: '))
print('Digite uma das bases para conversão: ')
print('\033[1m[ 1 ] converter para \033[1;31mBINÁRIO\033[m \n\033[1m[ 2 ] converter para \033[1;32mOCTAL\033[m \n\033[1m[ 3 ] converter para \033[1;33mHEXADECIMAL\033[m')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é {}.'.format(num, oct(num).upper()[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a \033[1m{}.'.format(num, hex(num).upper()[2:]))
else:
    print('Opção inválida, tente novamente.')