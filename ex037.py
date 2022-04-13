#  Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
#  escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Escreva um número: '))
choice = int(input('Digite'
                   '\n1 para binário '
                   '\n2 para octal '
                   '\n3 para hexadecimal'
                   '\n'))

if choice == 1:
    print('O número {} em binário fica {}.'.format(num, bin(num)))
elif choice == 2:
    print('O número {} em octal fica {}'.format(num, oct(num)))
elif choice == 3:
    print('O número {} em hexadecimal fica {}.'.format(num, hex(num)))
else:
    print('Você não escolheu nenhuma das opções. \nAssim não da!')
