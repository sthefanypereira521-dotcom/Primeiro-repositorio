from random import randint
vitorias = 0

while True:
    jogador = int(input('digite um valor:'))
    computador = randint(0, 10)
    total = jogador + computador

    tipo = ''
    while tipo != 'P' and tipo != 'I':
        tipo = str(input('par ou ímpar? [P/I] ')).strip().upper()[0]
    print(
        f'voce jogou {jogador} e o computador {computador}: total deu {total} ')

    if total % 2 == 0:
        resultado = 'P'
        print('deu par')

    else:
        resultado = 'I'
        print(' deu ímpar')

    if tipo == resultado:
        print(' VOCE VENCEU!!! ')
        vitorias += 1
        print(' bora jogar de novo...\n')

    else:
        print(' VOCE PERDEU:.')
        break

print(f'GAME OVER! voce venceu {vitorias } vezes. ')
