'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.'''
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

casa = float(input('Digite aqui o valor do imóvel: R$'))
salario = float(input('Digite o salário do comprador do imóvel: R$'))
anos = int(input('Quantos anos será parcelado: '))
minimo = salario * 30 /100
parcela = casa / (anos * 12)
print(f'Para pagar a casa de \033[1mR${casa}\033[m em \033[1m{anos}\033[m, a prestação será de \033[1;31m{parcela:.2f}\033[m.')
print(f'Comparando {parcela :.2f} - {minimo}')
if parcela <= minimo:
    print(f'Seu empréstimo foi \033[1;34mAPROVADO.\033[m')
elif parcela > minimo:
    print(f'Seu empréstimo foi \033[1;31mNEGADO.\033[m')
