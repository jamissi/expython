v = float(input('Informe a velocidade do carro: '))
if v > 80:
    print('Você foi multado por exceder o limite da via de 80Km/h.')
    m = (v - 80) * 7
    print(f'Você deve pagar a multa de R${m}')
print('Tenha um bom dia! Dirija com segurança.')