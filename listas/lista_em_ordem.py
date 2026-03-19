valores = []
for c in range(0, 5):
    numeros = int(input('digite um numero : '))
    if c == 0 or numeros > valores[-1]:
        valores.append(numeros)
        print('adicionando ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if numeros <= valores[pos]:
                valores.insert(pos, numeros)
                print(f'adicionando na posiçao {pos}  da lista')
                break
            pos += 1
print('-=-' * 18)
print(f' os numeros digitados em ordem foram {valores}')
