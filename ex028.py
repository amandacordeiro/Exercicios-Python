from random import randint
from time import sleep # faz o programa meio que ''dormir'' por alguns segundos

computador = randint(0, 5) # faz o computador pensar ''adivinhar''

print('-=-' * 20)

print('Olá, meu nome é Noble e eu sou encarregado de pensar em números.\n'
      'Será que você consegue pensar no mesmo número que eu?')

print('-=-' * 20)

usuario = int(input('Vamos lá! \nDigite um número entre 0 e 5: ')) # aqui o usuario tenta adivinhar

print('PROCESSANDO...')
sleep(3)

if usuario == computador:
      print('\nParabéns! Você conseguiu me vencer. XD')
else:
      print('\033[30;41mNão foi dessa vez.\033[m \nEu pensei no número {}. I WIN AND YOU LOSE!.'.format(computador))
