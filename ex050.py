soma = 0
count = 0

for c in range(1, 7):
    num = int(input('Digite o {} valor:'.format(c)))
    if num % 3 == 0:
        soma += num
        count += 1
print('Você informou {} números ÍMPARES e a soma foi de {}.'.format(count, soma))
