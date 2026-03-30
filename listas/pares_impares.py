numeros = [[], []]
valor = 0

for c in range(1, 8):
    valor = int(input(f'digite o {c}º  numero:'))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)

numeros[0].sort()
numeros[1].sort()

print(f' os valores pares:{numeros[0]} ')
print(f' os valores impares:{numeros[1]}')
