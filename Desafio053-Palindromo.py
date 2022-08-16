#Crie um programa que leia uma frase qualquer e diga
#Se ela é um palindromo, desconsiderando os espaços.
#Crie um programa que leia uma frase qualquer e diga
#Se ela é um palindromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto =''.join(palavras)
inverso = junto[::-1]
'''inverso = ''
for c in range (len(junto) -1, -1, -1):
    inverso += junto[c]'''
print(f'O inverso de {frase} é {inverso}.')
if inverso == frase:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')