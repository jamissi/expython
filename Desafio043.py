'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
-Abaixo do peso 18.5
-Peso ideal entre 18.5 e 25
- Sobrepeso 25 até 30
- Obesidade mórbida acima de 40'''

peso = float(input('Digite o seu peso (Kg): '))
altura = float(input('Digite sua altura (M): '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'O cálculo do IMC foi de {imc :.2f}. Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print(f'O cálculo do IMC foi de {imc :.2f}. Seu peso é ideal.')
elif 25 <= imc < 30:
    print(f'O cálculo do IMC foi de {imc :.2f}. Você está com sobrepeso.')
elif 30 <= imc < 40:
    print(f'O cálculo do IMC foi de {imc :.2f}. Procure um médico, você está obeso.')
else:
    print('VOCÊ ESTÁ EM OBESIDADE MÓRBIDA. CUIDADO, PROCURE AJUDA!')