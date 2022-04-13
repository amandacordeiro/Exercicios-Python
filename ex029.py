from time import sleep
import emoji

print((emoji.emojize(':cop: Olá!\nEu sou o seu guarda virtual que calcula multas.', use_aliases=True)))

vl = float(input(emoji.emojize('\nEm que velocidade você está dirigindo? :car: ', use_aliases=True)))


print('PROCESSANDO...')
sleep(3)

if vl > 80:
    print('\nCalma aí.\nVocê está ultrapassando a velocidade permitida.'
          '\nSua multa é de R${:.2f}.'
          '\nPara evitar outras multas, mantenha a velocidade em 80Km/H.'.format((vl - 80) * 7))
else:
    print('Tudo ok!\nVocê está digirindo conforme as leis.'
          '\nMantenha o ritmo para evitar multas.'
          '\nTenha um ótimo dia!')
