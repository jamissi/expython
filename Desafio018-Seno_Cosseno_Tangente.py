# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente

import math
an = float(input('Digite um ângulo: '))
sen = math.sin(math.radians(an))
cas = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print(f'O ângulo {an}, tem o valor de sen {sen :.2f}, cosseno {cas :.3f} e a tangente {tan :.4f}')
