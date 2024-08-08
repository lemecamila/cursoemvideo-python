

import random
import time
num = random.randint(0, 10)
n = 11
palpite = 0
while n != num:
    print('Tente advinhar o numero de 0 a 10 que o Pc está pensando')
    n = int(input('Digite seu chute:'))
    palpite = palpite + 1

    print('PROCESSANDO...')
    '''time.sleep(2)'''

    if n != num:
        print('Voce errou!')
        if n < num:
            print('É maior que isso. Tente novamente!')
        else:
            print('É menor que isso. Tente novamente!')

print('O Pc pensou no numero: {} e voce pensou no numero: {}'.format(num,n))
print('Parabéns voce acertou em {} tentantivas'.format(palpite))
print('-=-' * 20)
