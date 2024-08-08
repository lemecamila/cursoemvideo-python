#tres segmentos podem formar um triangulo?
reta1 = float(input('Digite o tamanho do primeiro segmento'))
reta2 = float(input('Digite o tamanho do segundo segmento'))
reta3 = float(input('Digite o tamanho do terceiro segmento'))


if ((reta1+reta2) > reta3) & ((reta1+reta3) > reta2) & ((reta2+reta3) > reta1):
    print('Os tres segmentos informados podem formar um triangulo')
else:
    print('Os tres segmentos informados nao podem formar um triangulo')

