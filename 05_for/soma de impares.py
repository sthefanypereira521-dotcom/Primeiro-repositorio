soma = 0
cont = 0

for c in range(0, 21, 2):
    print(c, end=' -> ')
# se o resto da divisao por 3 for zero,
# significa que o numero e divisivel por 3
    if c % 3 == 0:
        cont += 1
        soma += c
print('\n')
print(f' a soma de todos os  {cont} numeros e igual a {soma}.')
