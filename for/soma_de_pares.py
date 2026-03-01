soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('digite um número:'))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'voçê informou {cont} números PARES  e a soma foi {soma}')
