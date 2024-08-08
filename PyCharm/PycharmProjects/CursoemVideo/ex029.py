# programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
v = float(input('Qual a velocidade do carro?'))

if v <= 80:
    print('Voce nao sera multado')
else:
    print('Voce sera multado e o valor da multa sera {:.2f}'.format(7*(v-80)))

