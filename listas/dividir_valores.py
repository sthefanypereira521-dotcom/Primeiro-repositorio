numeros = []
pares = []
impares = []

while True:
    numeros.append(int(input('digite um numero: ')))
    resposta = str(input(' quer continuar? [S/N] '))

    if resposta in 'Nn':
        break
for i, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-=-' * 18)
print(f'a lista completa e {numeros}')
print(f'os pares sao {pares}')
print(f'os impares sao {impares}')
