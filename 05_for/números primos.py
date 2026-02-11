num = int(input('digite um número: '))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')  # amarelo for divisivel
        tot += 1
    else:
        print('\033[31m', end='')  # vermelho se nao for divisivel
    print(f" {c} ", end='')
print(f'\n\033[m o número {num} foi divisível {tot} vezes.')
if tot == 2:
    print('por isso ele é PRIMO!')
else:
    print('por isso ele NAO é PRIMO!')
