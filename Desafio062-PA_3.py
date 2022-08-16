print('-'* 10, 'P.A.', '-'* 10)
print('--- 10 PRIMEIROS TERMOS ---')
primeiro = int(input('\nDigite o 1° elemento: '))
razao = int(input('Digite a razão: '))
termos = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f' {termos} ->', end='')
        termos += razao
        cont += 1
    print(' ...')
    mais = int(input('''Quantos termos a mais você deseja mostrar?'''))
print(f'A P.A. foi finalizada e {total} termos foram mostrados.')
