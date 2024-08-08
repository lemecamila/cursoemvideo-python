#programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('Digite um numero para descobrir se é primo ou nao: '))
s=0
for c in range(1,num+1):
    if num % c  == 0:
        s = s + 1
    else:
        s = s

if s == 2:
    print('O número {} é um número primo!'.format(num))
else:
    print('O número {} nao é um número primo!'.format(num))