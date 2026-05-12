numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 23]

procurado = 15

inicio = 0
fim = len(numeros) - 1
encontrado = False

for _ in range(len(numeros)):
    print()
    if inicio > fim:
        break

    meio = (inicio + fim) // 2

    print(f'=' * 60)
    print(f'intervalo atual: {numeros[inicio:fim + 1]}')
    print(f'inicio no indice = {inicio}  fim do indice = {fim}')
    print(f'meio do indice = {meio}   valor do meio = {numeros[meio]}')
    print(f'=' * 60)
    print()

    if numeros[meio] == procurado:
        print(f'indice = {meio} ')
        print(f'numero encontrado = {numeros[meio]}')
        print()
        encontrado = True
        break

    elif numeros[meio] < procurado:
        inicio = meio + 1

    else:
        fim = meio - 1

if not encontrado:
    print('numero nao encontado...')
