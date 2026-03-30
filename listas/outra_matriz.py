matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = maior_valor = soma_coluna = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(
            input(f'digite um numero para [{linha}, {coluna}]:'))
print('-=-' * 16)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz [linha][coluna]:^6}]', end=' ')
        if matriz[linha][coluna] % 2 == 0:
            soma_par += matriz[linha][coluna]
    print()
print('-=-' * 16)
print(f'soma dos números pares é: {soma_par}')
for linha in range(0, 3):
    soma_coluna += matriz[linha][2]
print(f'soma dos números da 3ª coluna é: {soma_coluna}')
for coluna in range(0, 3):
    if coluna == 0:
        maior_valor = matriz[1][coluna]
    elif matriz[1][coluna] > maior_valor:
        maior_valor = matriz[1][coluna]
print(f'maior número da 2ª linha é: {maior_valor}')
