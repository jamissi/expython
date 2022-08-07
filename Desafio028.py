#import random
#n1 = int(input('Escolha um número entre 0 e 5: '))
#l1 = [0, 1, 2, 3, 4, 5]
#e1 = random.choice(l1)
#if n1 == e1:
#    print('Parabéns, você acertou!')
#else:
#    print('Tente novamente.')
#print('--FIM--')

from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador escolher um número
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? ')) # O jogador escolhe um número
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS, VOCÊ VENCEU! ): ')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}, tente novamente. :D')
