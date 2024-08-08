'''Faca um programa que leia um numero e mostre seu fatorial.
Faca uma resolucao com While e outra com For'''

'''Opcao While'''
num = int(input('Digite um numero inteiro para descobrir o seu fatorial: '))
c = num
fatorial = 1
print('Calculando {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print('x' if c>1 else ' = ', end='')
    fatorial = c * fatorial
    c = c - 1
print('{}'.format(fatorial))

'''Opcao For'''
'''num = int(input('Digite um numero inteiro para descobrir o seu fatorial: '))
c = 1
fatorial = 1
for c in range(1,num+1):
    fatorial = c * fatorial
    c = c + 1
print('O fatorial de {} é {}'.format(num,fatorial))'''

'''Importando Biblioteca'''
#
# from math import factorial
#
# num = int(input('Digite um numero inteiro para descobrir o seu fatorial: '))
# fatorial = factorial(num)
# print('O fatorial de {} é {}'.format(num,fatorial))

