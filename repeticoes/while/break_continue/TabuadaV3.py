while True:
    n = int(input('digite um numero pra ver a tabuada: '))
    print('-=-' * 13)

    if n < 0:
        break
    for c in range(1, 11):
        print(f' {n} x {c} = {n * c} ')
    print('-=-' * 13)

print('===PROGRAMA ENCERRADO===')
