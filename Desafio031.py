v = float(input('Digite a quilometragem da sua viagem: '))
if v <= 200:
    pu = v * 0.50
    print(f'O preço da sua passagem ficou em R${pu :.2f}')
else:
    pd = v * 0.45
    print(f'O preço da sua passagem ficou em R${pd :.2f}')

print('Tenha uma boa viagem!')