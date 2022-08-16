from random import randint
from time import sleep
n = 0
computador = randint(1, 10) # Faz o computador escolher um número
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? ')) # O jogador escolhe um número
while jogador != computador:
    print('PROCESSANDO...')
    sleep(0.5)
    print('\033[1;31mTente novamente\033[m')
    jogador = int(input('Em que numero eu pensei? '))
    n += 1
print('PROCESSANDO...')
sleep(0.5)
print(f'Eu pensei no número {computador}.')
print(f'\033[1;32mP\033[1;33mA\033[1;34mR\033[1;35mA\033[1;36mB\033[1;37mÉ\033[1;31mN\033[1;30mS\033[m, '
      f'\033[1mVOCÊ CONSEGUIU! \nForam necessários \033[1;34m{n}\033[m \033[1mpalpites para você acertar.')
