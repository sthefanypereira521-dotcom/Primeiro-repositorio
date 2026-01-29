numero = int(input('digite um numero qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('o numero {} e PAR'.format(numero))
else:
    print('o numero {} e IMPAR'.format(numero))