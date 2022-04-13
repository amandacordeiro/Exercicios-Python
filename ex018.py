from math import sin, cos, tan, radians

ang = (float(input('Digite o valor de um ângulo: ')))
seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))

print('Seu seno: {:.2f}'
      '\nSeu cosseno: {:.2f}'
      '\nSua tangente: {:.2f}'.format(seno, coss, tang))
