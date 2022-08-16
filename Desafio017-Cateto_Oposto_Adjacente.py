'''from math import sqrt

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = (pow(co,2)) + (pow(ca,2))
ch = sqrt(h)
print(f'O comprimento da hipotenusa é {ch :.1f}!')'''

import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = math.hypot(co, ca)
print(f'O comprimento da hipotenusa é {h :.1f}!')