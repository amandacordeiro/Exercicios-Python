print('Olá! \nPor gentileza, me informe o valor do seu salário para calcularmos a porcentagem.\n')

salario = float(input('Digite o valor aqui. R$'))

if salario >= 1250:
    novo = salario + (salario * 10 / 100)
else:
    novo = salario + (salario * 15 / 100)

print('Se você ganhava R${:.2f}, agora você começará a ganhar R${:.2f}.'.format(salario, novo))
