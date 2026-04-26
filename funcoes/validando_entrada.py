def leia_int(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31m ERRO! digite um numero valido.\033[m')
        if ok:
            break
    return valor


n = leia_int('digite um numero:')
print(f'voce digitou o numero {n}')
