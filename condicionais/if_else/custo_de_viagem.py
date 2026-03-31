distancia = float(input('qual e a distancia da viagem?'))
print('voce esta preste a começar a viagem de {}km'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('o preço da sua passagem sera de R${:.2f}'.format(preço))