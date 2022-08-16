'''Elabore um programa que calcule o valor a ser pago
por um produto, considerando o seu preço normal e condição de pagamento:
- A vista Dinheiro/Cheque: 10% de desconto
- A vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''

p = float(input('Digite aqui o valor do produto: R$'))
print('\nFormas de pagamento:')
print('\n1 - Dinheiro/Cheque \n2 - Á vista no cartão \n3 - 2x no cartão \n4 - 3x ou mais no cartão')
menu = input('')
#1
if menu == "1":
    p1 = p - (p * 0.1)
    print(f'O valor do produto terá \033[1;31;40m10% de desconto\033[m, o valor a ser pago é de \033[1;31;40mR${p1}\033[m.')
#2
elif menu == "2":
    p1 = p - (p*0.05)
    print(f'O valor do produto terá \033[1;31;40m5% de desconto\033[m, o valor a ser pago é de \033[1;31;40mR${p1}\033[m.')
#3
elif menu == "3":
    p1 = p
    parcela = p1/ 2
    print(f'Sua compra será parcela em 2x de R${parcela}.')
    print(f'\033[1;31mNão há desconto\033[m no valor do produto, então ele será \033[1;31mR${p}\033[m.')
#4
elif menu == "4":
    p1 = p + (p * 0.2)
    totparc = int(input('Quantas parcelas: '))
    parcela = p1 / totparc
    print(f'O valor será parcelado, terá um \033[1;31;40madicional de 20%\033[m. O total será de \033[1;31;40mR${p1}\033[m.')
    print(f'Sua compra será parcela em {totparc}x de R${parcela}. COM JUROS.')
else:
    print('Opção Inválida')
print('\nObrigada por escolher a \033[1;34;40mJucicleia Lojas\033[m. Volte sempre!')
