def busca_binaria(lista, valor):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        print(f'=' * 60)
        print(f'intervalo atual: {numeros[inicio:fim + 1]}')
        print(f'inicio no indice = {inicio}  fim do indice = {fim}')
        print(f'meio do indice = {meio}   valor do meio = {numeros[meio]}')
        print(f'=' * 60)
        print()

        if lista[meio] == valor:

            return f'numero encontrado na posiçao {meio}'

        elif lista[meio] < valor:
            inicio = meio + 1

        else:
            fim = meio - 1

    return 'numero nao encontrado'


numeros = [2, 5, 6, 9, 11, 13, 15, 22, 25, 26, 33, 45, 50]
print(busca_binaria(numeros, 25))
