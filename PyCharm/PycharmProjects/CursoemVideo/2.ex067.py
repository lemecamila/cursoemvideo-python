# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

n = 0
while True:
    print('-'*35)

    n = int(input('Quer ver a tabuada de qual valor? '))

    print('-'*35)

    if n<0:
        break

    cont = 0

    while cont < 10:
        cont += 1
        mult = n*cont
        print('{} x {} = {}'.format(n,cont,mult))

print('Fim do Programa')



