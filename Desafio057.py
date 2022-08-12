sexo = str(input('Digite seu sexo [M/F]: ')).upper()[0].strip()
while sexo != 'M' and sexo != 'F':
    print('Sexo Inválido.')
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()[0].strip()
print('FIM')
