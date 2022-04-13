import math
ang = float(input('Digite o ângulo que você deseja: '))

seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))

print('O ângulo de {} tem o SENO de {:.2f}'
      '\nO COSSENO de {:.2f}'
      '\nE a TANGENTE de {:.2f}'.format(ang, seno, cosseno, tangente))
