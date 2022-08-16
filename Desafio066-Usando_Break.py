n = c = s = 0
while True:
    n = int(input('Digite um n° inteiro: '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Você digitou {c} e a soma deles foi {s}!')

