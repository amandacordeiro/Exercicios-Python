# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e
# mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

import time
from datetime import date

print('Oi! Tudo bom? \nTô aqui pra te dizer em qual categoria você se encaixa.'
      '\nVou precisar que você me informe a sua idade, tudo bem?'
      '\nVamos lá então.')

idade_ano = int(input('Em que ano você nasceu? '))
calc = date.today().year - idade_ano

print('PROCESSANDO...')
time.sleep(2)

if calc < 9 or calc == 9:
    print('CATEGORIA MIRIM.'.format(calc))
elif calc <= 14:
    print('CATEGORIA INFANTIL.'.format(calc))
elif calc <= 19:
    print('CATEGORIA JÚNIOR.')
elif calc <= 25:
    print('CATEGORIA SENIOR.')
else:
    print('CATEGORIA MASTER.')
