real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.30
euro = real / 6.54
print('Com R${:.2f} você pode comprar US${:.2f} e EUR${:.2f}.'.format(real, dolar, euro))
