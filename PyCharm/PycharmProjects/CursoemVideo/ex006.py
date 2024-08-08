#le um numero e mostra o dobro, triplo e raiz quadrada
from math import sqrt
num = float(input('Digite um número: '))
print(f'O dobro do valor é: {num*2}')# .format(num*2))
print('O triplo do valor é: {}' .format(num*3))
print(f'A raiz quadara do valor é: {pow(num,(1/2)):.2f}') #.format(pow(num,(1/2))))
print('check raiz quadrada: {}' .format(sqrt(num)))

