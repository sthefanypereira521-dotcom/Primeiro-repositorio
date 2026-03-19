valores = list()
while True:
    n = int(input('digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('valor adicionado com sucesso...')
    else:
        print('valor duplicado!!!')
    r = str(input('quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('-=-' * 15)
valores.sort()
print(f'voce digitou os numeros: {valores} ')
