print('\033[33m✧･ﾟ: *✧･ﾟ:*\033[m' * 3)
print('Analisador de Triângulos')
print('\033[33m✧･ﾟ: *✧･ﾟ:*\033[m' * 3)

r1 = float(input('\nPrimeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar triângulos.\n')
else:
    print('Os segmentos não podem formar triângulos.\n')

print('\033[33m✧･ﾟ: *✧･ﾟ:*\033[m' * 3)
print('Esse triàngulo é um: ')

if r1 == r2 and r2 == r3 and r1 == r3:
    print('Equilátero')
elif r1 != r2 and r2 != r3 and r1 != r3:
    print('Escaleno')
else:
    print('Isósceles')
