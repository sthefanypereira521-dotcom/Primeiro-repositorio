pessoas = {}
grupo = []
soma = media = 0

while True:
    pessoas.clear()
    pessoas['nome'] = str(input('nome:'))

    while True:
        pessoas['sexo'] = str(input('sexo:[M/F] ')).upper()
        if pessoas['sexo'] in 'MF':
            break
        print('ERRO! digite apenas M ou  F:')
    pessoas['idade'] = int(input('idade:'))
    soma += pessoas['idade']
    grupo.append(pessoas.copy())

    while True:
        resposta = str(input('quer continuar? [S/N] ')).upper()
        if resposta in 'SN':
            break
        print('ERRO! apenas S ou  N: ')
    if resposta == 'N':
        break
print('-=-' * 15)

print(f' ao todo temos {len(grupo)} pessoas cadastradas: ')
media = soma/len(grupo)
print(f' a media de idade e de {media:5.2f} anos. ')
print(' as mulheres cadastradas foram: ', end=' ')

for p in grupo:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()

print(' lista de pessoas acima da media:', end=' ')
for p in grupo:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}: ', end=' ')
        print()
print('===-ENCERRADO-===')
