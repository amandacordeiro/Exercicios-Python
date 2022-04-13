print('{:=^40}'.format(' LOJAS GUANABARA '))

preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

opção = int(input('Qual é a opção? '))

if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    total_parcelas = int(input('Quantas parcelas? '))
    parcela = total / total_parcelas
    print('Sua compra será parcelada em {}x vezes de R${:.2f} COM JUROS.'.format(total_parcelas, parcela))
else:
    total = 0
    print('Opção inválida de pagamento. Tente novamente.')

print('Sua compra de R$ {:.2f} vai custar R$ {:.2f}.'.format(preço, total))
