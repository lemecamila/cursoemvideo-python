# Faça um programa que jogue par ou ímpar com o computador.O jogo
# só será interrompido quando o jogador perder, mostrando o total
# de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
v = 0
while True:
    print('VAMOS JOGAR PAR OU ÍMPAR\n')
    n1 = int(input('Digite uma valor: '))
    resp = ' '
    while resp not in 'PI':
        resp = str(input('Voce escolhe PAR ou IMPAR? [P/I]\n')).strip().upper()[0]
    n2 = randint(0,10)
    soma = n1 + n2
    if soma%2 == 0:
        print(f'Voce digitou {n1} e o computador pensou em {n2}. A somatória é {soma}. Deu PAR \n')
        if resp == 'P':
            print('Voce acertou!! Parabéns')
            v += 1
        else:
            print('Que pena, voce errou! \n FIM DO JOGO')
            break
    else:
        print(f'Voce digitou {n1} e o computador pensou em {n2}. A somatória é {soma}. Deu IMPAR \n ')
        if resp == 'I':
            print('Voce acertou!! Parabéns')
            v += 1
        else:
            print('Que pena, voce errou! \n FIM DO JOGO')
            break
print( f'Voce venceu {v} vezes')


