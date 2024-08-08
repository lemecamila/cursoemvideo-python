vlr = int(input('Digite o numero que gostaria de calcular a tabuada: '))
print('A tabuada de {} é: '.format(vlr))

for c in range (1,10):
    print('{} x {:.2f} = {:.2f}'.format(c, vlr, vlr*c))