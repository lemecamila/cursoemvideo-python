#programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual
# foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random #opcao: from radom import randint
from time import sleep

num = int(random.randrange(0,5)) #opcao: num = randint(0,5)


print('Tente advinhar o numero de 0 a 5 que o Pc está pensando')
n = int(input('Digite seu chute:'))
print('-=-'*20)
print('O Pc pensou no numero: {}'.format(num))
print('PROCESSANDO...')
sleep(3)
print('Voce acertou' if num == n else 'Voce errou')


