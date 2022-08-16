ph = str(input('Enter a phrase: ')).upper().strip()
print('There is {} letter A in phrase, '.format(ph.count('A')))
print('The first A appear in the position, {}'.format(ph.find('A') + 1))
print('The last A appear in the position {}'.format(ph.rfind('A') + 1))