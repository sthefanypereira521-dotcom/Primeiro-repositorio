listagem = ('PC', 1300,
            'monitor', 500,
            'mesa L', 200,
            'teclado', 150,
            'mouse', 100,
            'mouse pad', 50,
            'filtro de linha', 40,
            'luminaria', 30)
print('-=-' * 18)
print(f'{"LISTA DE PREÇOS":^50}')
print('-=-' * 18)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-=-' * 18)
