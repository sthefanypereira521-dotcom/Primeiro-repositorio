num = int(input('digite um numero inteiro: '))

print(''' escolha uma das bases para converção:
[ 1 ]  converter para BINÁRIO
[ 2 ]  converter para OCTAL
[ 3 ]  converter para HEXADECIMAL ''')

opção = int(input('sua opção:'))

if opção == 1:
    print(f'{num} convertido para BINÁRIO É igual a {bin(num)} ')
elif opção == 2:
    print(f'{num} convertido para OCTAL É igual a {oct(num)} ')
elif opção == 3:
    print(f'{num} corvertido para HEXADECIMAL É igual a {hex(num)} ')
else:
    print('OPÇÃO INVALIDA!!')
