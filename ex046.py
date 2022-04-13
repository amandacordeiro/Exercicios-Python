import time

print('Vai começar agora a contagem regressiva para os fogos de artifício.')

for c in range(10, -1, -1):
    time.sleep(1)
    print(c)

print('COMEÇOU!')
