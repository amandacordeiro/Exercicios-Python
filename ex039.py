# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input('Em que ano você nasceu? '))
calc = date.today().year - ano

if calc < 18:
    print('Ainda não chegou a hora de você se alistar. \nFaltam {} anos.'.format(18 - calc))
elif calc == 18:
    print('Parabéns! Está na hora de se alistar.'.format(calc))
else:
    print('Você já passou do tempo de alistamento. \nFica pra uma próxima vida XD.')
