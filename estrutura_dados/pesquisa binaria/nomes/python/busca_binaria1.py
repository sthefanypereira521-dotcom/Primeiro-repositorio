nomes = ['ana', 'beatriz', 'bruna', 'carlos', 'daniel', 'emilie']

nome_buscar = input('digite um nome para buscar:').strip().lower()

esquerda = 0
direita = len(nomes) - 1

rodada = 1
encontrado = False

while esquerda <= direita:
    print(f'\nrodada {rodada}')
    print('intervalo atual:')

    for i in range(esquerda, direita + 1):
        print(nomes[i], end=' ')
    print()

    meio = (esquerda + direita) // 2
    print(f'meio atual: {nomes[meio]}')

    if nomes[meio] == nome_buscar:

        encontrado = True
        print('nome encontrado')
        break

    elif nomes[meio] < nome_buscar:
        print(f'{nomes[meio]} < {nome_buscar}, buscando a direita...')

        esquerda = meio + 1

    else:
        print(f'{nomes[meio]} > {nome_buscar}, buscando a esquerda...')
        direita = meio - 1

    rodada += 1

if not encontrado:
    print('nome nao encontrado!!')
