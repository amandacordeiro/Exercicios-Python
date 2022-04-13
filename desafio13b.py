s = float(input('Qual é o valor do seu salário? R$ '))
a = float(input('Quanto custa o produto que você quer comprar? R$ '))
s1 = s + (s * 5 / 100)
a1 = a - (a * 10 / 100)
a2 = a + (a * 8 / 100)
print('Seu salário com aumento de 5% é {:.2f}R$.'.format(s1))
print('O produto que você quer comprar custa {:.2f}R$ com desconto, e {:.2f}R$ parcelado.'
      .format(a1, a2))

