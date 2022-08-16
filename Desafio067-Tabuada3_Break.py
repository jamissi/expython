while True:
    print('-*' * 20)
    n = int(input('Digite um n° para saber sua tabuada: '))
    print('-*' * 20)
    if n < 0:
        break
    for c in range(1, 11):
        s = n * c
        print(f'{n} x {c} = {s}')
print('-'*20,'Programa Encerrado', '-'*20)