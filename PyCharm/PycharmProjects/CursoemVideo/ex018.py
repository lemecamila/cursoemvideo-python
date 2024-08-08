#dado o angulo calcule seno, cosseno e tangente
import math
ang = float(input('Digite o valor, em rad, do angulo'))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('O seno do angulo é: {:.2f}. O cosseno do angulo é: {:.2f}. A tangente do angulo é: {:.2f}'
      .format(seno, cos,tan))


