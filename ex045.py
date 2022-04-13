from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('O computador escolheu {}'.format(itens[computador]))

print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

jogador = int(input('Qual é a sua jogada? '))
if jogador != 0 and jogador != 1 and jogador != 2:
    print('JOGADA INVÁLIDA.')

else:
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))

if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!')

elif computador == 1:
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCEU!')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
