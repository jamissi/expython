import random
import emoji
print(emoji.emojize('VAMOS JOGAR JOKEMPO :fist: :hand: :v:!!', language='alias'))
ppt = str(input(emoji.emojize('Digite: \n1 para \033[1;33mPedra :fist:\033[m \n2 para \033[1;34mPapel :hand:\033[m \n3 para \033[1;31mTesoura :v:\033[m\n= ',language='alias')))
lista = ['PEDRA', 'PAPEL', 'TESOURA']
pc = random.choice(lista)
# PEDRA
if ppt == '1' and pc == 'PEDRA':
    print(emoji.emojize('\033[1;33mEMPATAMOS. :fist: + :fist:', language='alias'))

elif ppt == '1' and pc == 'PAPEL':
    print(emoji.emojize(
        'Eu escolhi \033[1;34mpapel :hand:\033[m e você \033[1;33mpedra :fist:\033[m. \033[1;32mEU GANHEI\033[m.',
        language='alias'))

elif ppt == '1' and pc == 'TESOURA':
    print(emoji.emojize(
        'Eu escolhi \033[1;31mtesoura :v:\033[me você \033[1;33mpedra :fist:\033[m. \033[1;35mVOCÊ GANHOU\033[m!!!!',
        language='alias'))
# PAPEL
elif ppt == '2' and pc == 'PAPEL':
    print(emoji.emojize('\033[1;34mEMPATAMOS. :hand: + :hand:', language='alias'))

elif ppt == '2' and pc == 'PEDRA':
    print(emoji.emojize(
        'Eu escolhi \033[1;33mpedra :fist:\033[m e você \033[1;34mpapel :hand:\033[m. \033[1;35mVOCÊ GANHOU\033[m!!!!',
        language='alias'))

elif ppt == '2' and pc == 'TESOURA':
    print(emoji.emojize(
        'Eu escolhi \033[1;31mtesoura :v:\033[m e você \033[1;33mpapel :hand:\033[m. \033[1;32mEU GANHEI\033[m.',
        language='alias'))
# TESOURA
elif ppt == '3' and pc == 'TESOURA':
    print(emoji.emojize('\033[1;31mEMPATAMOS :v: + :v:', language='alias'))

elif ppt == '3' and pc == 'PEDRA':
    print(emoji.emojize('\033[1;32mEU GANHEI :v: + :fist:. QUE PENA :D!', language='alias'))

elif ppt == '3' and pc == 'PAPEL':
    print(emoji.emojize('\033[1;35mVOCÊ GANHOU :v: + :hand:, PARABÉNS!!!', language='alias'))
