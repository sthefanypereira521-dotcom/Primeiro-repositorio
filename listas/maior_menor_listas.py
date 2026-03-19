valores = []
maior = 0
menor = 0
for c in range(0, 5):
    valores.append(int(input(f'digite um valor para a posiçao {c}: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print('-=-' * 15)
print(f' voce digitou  os valores {valores}')
print(f'maior valor digitado {maior} nas posiçoes ', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'o menor valor digitado {menor} nas posiçoes ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()
