#homem
maioridadem = 0
nomevm = 0
# média idade
somaidade = 0
mediaidade = 0
# quantas mulheres tem 20 anos
totmulher = 0

for c in range (1,5):
    print(f'----{c}º PESSOA----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M]/[F]:'))
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadem = idade
        nomevm = nome
    if sexo in 'Mm' and idade > maioridadem:
        maioridadem = idade
        nomevm = nome
    if sexo in 'Ff' and idade < 20:
        totmulher += 1
mediaidade = somaidade/4
print(f'A média da idade do grupo é: {mediaidade}')
print(f'O homem mais velho se chama {nomevm} e tem {maioridadem} anos.')
print(f'Existe(em) {totmulher} mulheres com menos de 20 anos.')
