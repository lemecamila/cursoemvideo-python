#dada a largura e a altura de uma parede, calule a área e a quantidade de litros de tinta necessários para
#para pintar a parede, sabendo que 1l pinta 2m2
larg = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))

print('A área da parede é {:.2f}m2'.format(larg*altura))
print('Voce precisará de {} litros de tinta para pitar toda a parede'.format(larg*altura/2))
