#leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
a = float(input('Digite o cateto oposto do triangulo retangulo'))
b = float(input('Digite o cateto adjacente do triangulo retangulo'))
'''print('Para o Triangulo retangulo com o cateto oposto de {} e o cateto adjacente {}, a hipotenusa vale {}'
.format(a,b,(a**2+b**2)**0.5))'''

import math
print('Para o Triangulo retangulo com o cateto oposto de {} e o cateto adjacente {}, a hipotenusa vale {}'
      .format(a,b,math.hypot(a,b)))
