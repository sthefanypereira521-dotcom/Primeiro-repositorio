print('-=-' * 10)
print(' SEQUÊNCIA DE FIBONACCI ')
print('-=-' * 10)

n = int(input('\nquantos termos voçe quer mostrar? '))
t1 = 0
t2 = 1
print('=-' * 50)

print(f'{t1} \033[1;31m => \033[m {t2}', end='')
cont = 3

while cont <= n:
    t3 = t1 + t2
    print(f' \033[1;31m => \033[m {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1

print('\033[1;31m => \033[m FIM')
print('=-' * 50)
