total = totmil = menor = cont = 0
barato = ' '

while True:
    produto = str(input('nome do produto: '))
    preco = float(input('preco: R$ '))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:=^40}'.format('fim de programa'))
print(f' total foi R${total:.2f} ')
print(f'temos {totmil} produtos acima de R$1000.00 ')
print(f' produto mais barato {barato} custa: R${menor:.2f}')
