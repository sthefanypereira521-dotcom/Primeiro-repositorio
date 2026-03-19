pessoal = list()
dado = list()
total_maior = total_menor = 0

for c in range(0, 3):
    dado.append(str(input('nome: ')))
    dado.append(int(input('idade: ')))
    pessoal.append(dado[:])
    dado.clear()

for p in pessoal:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade. ')
        total_maior += 1
    else:
        print(f'{p[0]} é menor de idade. ')
        total_menor += 1

print(f'temos {total_maior} maiores e \n{total_menor} menores de idade: ')
