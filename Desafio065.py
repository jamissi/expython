cont = soma = media = menu = maior = menor = 0
while menu != 'N':
    cont += 1
    num = int(input('Digite um número: '))
    menu = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media = soma / cont
print(f'''Você digitou {cont} e soma deles é {soma}.
A média foi {media :.1f}.
Esse é {maior} maior número e {menor} esse foi menor.''')


