import random
from time import sleep
print('Vamos jogar Jokenpo!!')
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
opcao = ('Pedra','Papel', 'Tesoura')
escolha1 = int(input('Primeiramente, digite o numero da sua escolha: \n'
                     'Sendo que: \n'
                     '(1) Pedra \n'
                     '(2) Papel \n'
                     '(3) Tesoura \n'))

if escolha1 != 1 and escolha1 != 2 and escolha1 != 3:
    print('Voce digitou uma opcao invalida!')
else:
    print('*-'*16)
    print('Voce escolheu {}'.format(opcao[escolha1-1]))
#if escolha1 == 1:
 #   nome1 = 'Pedra'
#elif escolha1 == 2:
  #  nome1 = 'Papel'
#else:
  #  nome1 = 'Tesoura'

    escolha2 = random.randrange(1,3,1)
    print('O Computador escolheu {}'.format(opcao[escolha2-1]))
    print('*-'*16)
#if escolha2 == 1:
   # nome2 = 'Pedra'
#elif escolha2 == 2:
   # nome2 = 'Papel'
#else:
 #   nome2 = 'Tesoura'

#print('Voce escolheu: {}'.format(nome1))
#print('O computador escolheu: {}'.format(nome2))

#if escolha1 == escolha2:
   # print('Houve um empate!')
#elif escolha1 == 1 and escolha2 ==2:
 #   print('O computador venceu!')
#elif escolha1 == 2 and escolha2 == 1:
#    print('Voce venceu!')
#elif escolha1 == 1 and escolha2 == 3:
  #  print('Voce venceu!')
#elif escolha1 == 3 and escolha2 == 1:
  #  print('O computador venceu!')
#elif escolha1 == 2 and escolha2 == 3:
 #   print('O computador venceu!')
#    print('Voce venceu!')
    sleep(2)
    if escolha1 == escolha2:
        print('Houve um empate!')
    elif escolha1 == 1 and escolha2 ==2 or escolha1 == 3 and escolha2 == 1 or escolha1 == 2 and escolha2 == 3 :
        print('O computador venceu!')
    else:
        print('Voce venceu!')

