from time import sleep
n1 = int(input(' primeiro valor: '))
n2 = int(input(' segundo valor: '))
opção = 0

while opção != 5:
    print('''    [ 1 ] somar 
    [ 2 ] multipicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('>>>> sua opção é?  '))
    if opção == 1:
        soma = n1 + n2
        print(f' a soma e {soma}')
    elif opção == 2:
        produto = n1 * n2
        print(f' o resultado é {produto}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f' entre {n1} e {n2} o maior valor é {maior}')
    elif opção == 4:
        print('informe os números novamente: ')
        n1 = int(input(' primeiro valor: '))
        n2 = int(input(' segundo valor: '))
    elif opção == 5:
        print('finalizando... ')
    else:
        print(' opção invalida tente novamente: ')
    print('=-=' * 12)
    sleep(2)

print('FIM DE PROGRAMA!!')
