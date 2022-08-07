#n = str(input('Enter a number between 0 to 9999: ')).strip()
#num = int(input('Enter a number between 0 to 9999: '))
#n = num(str)
#print('Units:{}'.format(n[3]))
#print('Tens:{}'.format(n[2]))
#print('Hundreds:{}'.format(n[1]))
#print('Thousands:{}'.format(n[0]))
num = int(input('Enter a number between 0 to 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Units:{}'.format(u))
print('Tens:{}'.format(d))
print('Hundreds:{}'.format(c))
print('Thousands:{}'.format(m))