

cont = soma = 0
resp = 'S'
maior = menor = 0

while resp != 'N':
    num = int(input('Digite um valor:'))

    cont = cont + 1
    soma = soma + num

    if cont == 1:
        menor = maior = num
    else:
        if num > maior:
            maior = num

        if num < menor:
            menor = num

    resp = str(input('Gostaria de continuar [S/N]:')).upper().strip()[0]

media = soma / cont
if menor == maior:
    print(
        'Voce digitou {} numeros, a media entre eles é {}, os numeros digitados sao iguais'.format(cont, media))
else:
    print('Voce digitou {} numeros, a media entre eles é {}, o maior valor é {} e o menor valor é {}'.format(cont,media,maior,menor))


