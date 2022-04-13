horario = float(input('Qual é o horário? '))

# testando a condição uma única vez com o if

if 0 < horario < 6:
    print('Você está no horário da madrugada.')
else:
    print('Você não está no horário da madrugada.')

# testando a condição em loop com while

while 0 < horario < 6:
    print('Você está no horário da madrugada.')
    horario = horario + 2
else:
    print('Você não está no horário da madrugada.')

# o while permite continuar decrementando o número de pipocas até chegar em 0:

num_pipocas = int(input('Digite o número de pipocas: '))

while num_pipocas > 0:
    print('O número de pipocas é: ', num_pipocas)
    num_pipocas = num_pipocas - 1

# o exemplo abaixo não aceita um salário menor do que o mínimo atual:

salario = int(input('Digite seu salário: '))
while salario < 998.0:
    salario = float(input('Entre com um salário MAIOR do que 998.00: '))
else:
    print('O salário que você entrou foi: ', salario)

# o exemplo abaixo só sai do loop quando o usuário digitar "OK"

resposta = input('Digite OK: ')

while resposta != 'OK':
    resposta = input('Não foi isso que a sua mommy pediu, vamos lá, digite OK: ')

# Declaramos um contador como 0:
contador = 0
# Definimos o número de repetições:
numero = int(input('Digite um numero: '))
# Rodamos o while até o contador se igualar ao número de repetições:
while contador < numero:
    print(contador)
    contador = contador + 1

while True:
    resposta = input('Digite OK: ')
    if resposta == 'OK':
        break
