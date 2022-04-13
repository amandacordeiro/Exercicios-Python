from math import hypot

catop = float(input('Informe o número do cateto oposto: '))
catad = float(input('Informe o número do cateto adjacente: '))

print('A hipotenusa do triângulo tem o valor de {:.0f}'.format(hypot(catop, catad)))

import math

catop = float(input('Informe o número do cateto oposto: '))
catad = float(input('Informe o número do cateto adjacente: '))
hi = math.hypot(catop, catad)

print('A hipotenusa do triângulo tem o valor de {:.2f}'.format(hi))
