from random import sample

n1 = input('\nPrimeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

print('A ordem de apresentação é de {}.'.format(sample((n1, n2, n3, n4), k=4)))

'''
import random

n1 = input('\nPrimeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
'''