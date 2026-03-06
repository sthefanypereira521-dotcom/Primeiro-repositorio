num = (int(input('digite 1º numero:')),
       int(input('digite 2º numero:')),
       int(input('digite 3º numero:')),
       int(input('digite 4º numero:')))
print(f'voce digitou os numeros: {num}')

print(f'o numero 9 apareceu {num.count(9)} vezes: ')
if 3 in num:
    print(f'o numero 3 apareceu na {num.index(3)+1}ª posiçao: ')
else:
    print(f'o numero 3 nao foi digitado em nenhuma posiçao:')

print('os numeros pares digitados foi:', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
