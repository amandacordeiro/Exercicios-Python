# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite o seu peso mais recente: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Abaixo do peso'.format(imc))
elif imc < 25:
    print('Peso ideal'.format(imc))
elif imc < 30:
    print('Sobrepeso'.format(imc))
elif imc < 40:
    print('Obesidade'.format(imc))
else:
    print('Obesidade mórbida'.format(imc))
