import emoji

print((emoji.emojize("Oi! :cop: \nEstou aqui para te ajudar a calcular o valor da sua passagem.",
                     use_aliases=True)))

distance = float(input('\nDigite o valor da distância em Km/H: '))

if distance <= 200:
    print('A passagem custa R${:.2f}'.format(distance * 0.50))
else:
    print('A passagem custa R${:.2f}'.format(distance * 0.45))

#preço = distance * 50 if distance <= 200 else distance * 0.45 #substitui isso no format.
