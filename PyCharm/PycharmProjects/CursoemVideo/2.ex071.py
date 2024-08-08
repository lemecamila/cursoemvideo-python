

print('CAIXA ELETRONICO')

while True:
    valor = int(input('Qual valor deseja sacar?'))

    vlr1 = int(valor/50)
    vlr2 = int((valor - vlr1*50)/20)
    vlr3 = int((valor - vlr1*50 - vlr2*20)/10)
    vlr4 = valor - vlr1*50 - vlr2*20 - vlr3*10

    print(f'Voce precisara sacar: \n '
      f'Cedulas de R$50: {vlr1}xR$50 = R${vlr1*50} \n'
      f'Cedulas de R$20: {vlr2}xR$20 = R${vlr2*20} \n'
      f'Cedulas de R$10: {vlr3}xR$10 = R${vlr3*10} \n'
      f'Cedulas de R$1: {vlr4}xR$1 = R${vlr4} \n'
      f'Totalizando R${vlr1*50 + vlr2*20 + vlr3*10 + vlr4},00')

    resp = str(input('Gostaria de sacar mais algum valor? [S/N]')).strip().upper()
    if resp[0] == 'N':
        break

