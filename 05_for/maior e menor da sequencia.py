maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'peso da {p}ª pessoa:'))
    if p == 1:            # primeira pessoa: serve como base para maior e menor peso
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'o maior peso foi {maior}kg')
print(f'o menor peso foi {menor}kg')
