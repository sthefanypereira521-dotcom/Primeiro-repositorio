def busca_binaria(nomes, nome_buscar):
    esquerda = 0
    direita = len(nomes) - 1

    rodada = 1

    while esquerda <= direita:
        print(f'\nrodada {rodada}')
        print('intervalo atual:')

        for i in range(esquerda, direita + 1):
            print(nomes[i], end=' ')
        print()

        meio = (esquerda + direita) // 2
        print(f'meio atual: {nomes[meio]}')

        if nomes[meio] == nome_buscar:
            print('nome encontrado!!!')

            return

        elif nomes[meio] < nome_buscar:
            print(f'{nomes[meio]} < {nome_buscar}, buscando a direita...')
            esquerda = meio + 1
        else:
            print(f'{nomes[meio]} < {nome_buscar}, buscando a esquerda...')
            direita = meio - 1

        rodada += 1

    print('nome nao encontrado....')


nomes = ['joao', 'jose', 'kayke', 'leo', 'maria', 'mario']

nome = input('digite um nome para buscar:').strip().lower()

busca_binaria(nomes, nome)
