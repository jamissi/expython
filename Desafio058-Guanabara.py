from random import randint
computador = randint(0, 10)
print('Vamos jogar. Pensei em um número entre 0 e 10.')
print('Adivinhe qual foi o número...')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('\nQual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente.')
        else:
            print('Menos... Tente novamente.')
print(f'\033[1;32mP\033[1;33mA\033[1;34mR\033[1;35mA\033[1;36mB\033[1;37mÉ\033[1;31mN\033[1;30mS\033[m, '
      f'\033[1mVOCÊ CONSEGUIU! \nForam necessários \033[1;34m{palpites}\033[m \033[1mpalpites para você acertar.')