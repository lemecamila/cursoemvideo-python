'''– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes'''

reta1 = float(input('Digite o tamanho do primeiro segmento: '))
reta2 = float(input('Digite o tamanho do segundo segmento: '))
reta3 = float(input('Digite o tamanho do terceiro segmento: '))

if ((reta1+reta2) > reta3) & ((reta1+reta3) > reta2) & ((reta2+reta3) > reta1):
    print('Os tres segmentos informados podem formar um triangulo')

    if reta1 == reta2 == reta3:
        print('Se trata de um triangulo EQUILATERO')

    elif reta1 != reta3 and reta2 != reta3 and reta1 != reta2:
        print('Se trata de um triangulo ESCALENO')

    else:
        print('Se trata de um triangulo ISOCELES')

else:
    print('Os tres segmentos informados nao podem formar um triangulo')