matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(
            input(f'digite um numero para [{linha}, {coluna}]:'))
print('-=-' * 16)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz [linha][coluna]:^6}]', end=' ')
    print()
