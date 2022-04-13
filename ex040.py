# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO
import time

n1 = float(input('Digite sua nota da N1: '))
n2 = float(input('Digite sua nota da N2: '))
c = (n1 + n2) / 2

print('PROCESSANDO...')
time.sleep(3)

print('Sua média é: {:.1f}'.format(c))

if c < 5.0:
    print('\033[1;31mREPROVADO.\033[m'.format(c))
elif c == 5.0 or c <= 6.9:
    print('\033[1;33mRECUPERAÇÃO.\033[m'.format(c))
elif c >= 7.0:
    print('\033[1;32mAPROVADO! EBA.\033[m'.format(c))
