print('\033[1;30;45mFaça um programa que leia o nome de uma pessoa, e mostre o primeiro e o último nome.\033[m')

nome = str(input('\033[1;30;45mDigite o seu nome completo: \033[m')).strip().lower().title().split()


print('O seu primeiro nome é {}.'.format(nome[0]))
print('O seu último nome é {}.'.format(nome[len(nome)-1]))
