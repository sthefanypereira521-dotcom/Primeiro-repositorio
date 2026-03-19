numeros = []
while True:
    numeros.append(int(input('digite um valor: ')))
    resposta = str(input('quer continuar? [S/N] '))
    if resposta in 'Nn':
        break
print('-=-' * 16)
print(f'voce digitou {len(numeros)} valores.')
numeros.sort(reverse=True)
print(f'os valores em ordem decrescente sao: {numeros}')
if 8 in numeros:
    print('sim, o 8 faz parte da lista!!!')
else:
    print('nao, o 8 nao faz parte da lista...')
