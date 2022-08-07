#Aumentos multiplos

salario = float(input('Digite o valor do salário do funcionário: R$'))
if salario <= 1250:
    aumento = salario + ((salario * 15) / 100)
    print(f'O salário de R${salario} irá aumentar 15%, então passará a ser R${aumento}.')
else:
    aumento = salario + ((salario * 10) / 100)
    print(f'O salário de R${salario} irá aumentar 10%, então passará a ser R${aumento}.')
