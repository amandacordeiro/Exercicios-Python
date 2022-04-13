# Crie um algorítmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n1 = int(input('Digite um número: '))
d = n1 * 2
t = n1 * 3
rq = n1 ** (1/2)
print('O número é {}, o dobro é {}, o triplo é {} e sua raiz quadrada é {:.2f}.'.format(n1, d, t, rq))
# comentario de resolução
# n = int(input('Digite um número: '))
# print('O número é {}, o dobro é {}, o triplo é {} e sua raiz quadrada é {:.2f}.'.format(n, (n*2), (n*3), (n**(1/2)))
# função pow também calcula raiz quadrada. ex: pow(n, (1/2)
