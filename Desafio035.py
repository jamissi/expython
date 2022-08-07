#Formando triângulos

a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))
if a + b > c and b + c > a and a + c > b:
    print('As medidas podem formar um triângulo!')
else:
    print('As medidas não podem formar um triângulo! :( ')
