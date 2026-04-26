from time import sleep


def maior(* num):
    cont = maior = 0

    print('=' * 50)
    print('analisando os numeros...')

    for valor in num:
        print(f'   {valor}', end=' ', flush=True)
        sleep(0.5)

        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1

    if cont == 0:
        print('nenhum numero foi informado:')

    else:
        print(f'\nforam informados {cont} numeros ao todo.')
        print(f'o maior numero informado foi {maior}.')

    print('=' * 50)
    print()
    print()


maior(5, 8, 1, 4)

maior(2, 9, 3)

maior(6, 7, 0)

maior()
