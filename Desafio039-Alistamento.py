from datetime import date
atual = date.today().year
ano = int(input('ANO DE SEU NASCIMENTO: '))
idade = atual - ano
print(f'Quem nasceu em \033[31m{ano}\033[m tem \033[32m{idade}\033[m anos em \033[33m{atual}\033[m.')
if idade == 18:
    print('Você tem que se alistar \033[1;31mIMEDIATAMENTE.\033[m')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam \033[1;34m{saldo} anos\033[m para o alistamento.')
    ano1 = saldo + atual
    print(f'\033[1;34mSeu alistamento será em {ano1}.')
elif idade > 18:
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há \033[1;31m{saldo} anos.')
    ano1 = atual - saldo
    print(f'Seu alistamento foi em {ano1}.')