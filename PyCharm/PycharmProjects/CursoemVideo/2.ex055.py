
maior = 0
menor = 0
for c in range(0,5):
    peso = float(input('Digite o peso da pessoa (kg): '))

    if peso > maior:
        maior = peso
        menor = menor

    else:
        maior = maior
        menor = peso


print('O maior peso digitado é: {}kg e o menor é: {}kg'.format(maior,menor))
