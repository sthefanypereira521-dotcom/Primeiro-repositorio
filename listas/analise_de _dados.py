pessoas = []
lista = []


maior_peso = 0
menor_peso = 0

while True:
    nome = str(input('nome:'))
    peso = float(input('peso:'))

    pessoas.append(nome)
    pessoas.append(peso)

    # copiando a lista e depois limpando
    lista.append(pessoas[:])
    pessoas.clear()

    # primeira pessoa define base
    if len(lista) == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

    resp = str(input('quer continuar? [S/N]'))
    if resp in 'Nn':
        break


print(f'Maior peso: {maior_peso}kg', end=' ')
for p in lista:
    if p[1] == maior_peso:
        print(f'[{p[0]}]', end=' ')
print()

print(f'Menor peso: {menor_peso}kg', end=' ')
for p in lista:
    if p[1] == menor_peso:
        print(f'[{p[0]}]', end=' ')
print()
