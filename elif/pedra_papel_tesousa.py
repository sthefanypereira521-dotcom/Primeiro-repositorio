from random import randint

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)

print('''suas opções:
[ 0 ]  PEDRA  
[ 1 ]  PAPEL
[ 2 ]  TESOURA ''')
JOGADOR = int(input('qual é a sua jogada? '))

print('-=' * 13)
print(f'computador jogou {itens[computador]} ')
print(f'JOGADOR jogou {itens[JOGADOR]} ')
print('-=' * 13)

if computador == 0:
    if JOGADOR == 0:
        print('empate')
    elif JOGADOR == 1:
        print('JOGADOR VENCE')
    elif JOGADOR == 2:
        print('computador VENCE')
    else:
        print('jogada INVÁLIDA')
elif computador == 1:

    if JOGADOR == 0:
        print('COMPUTADOR VENCE')
    elif JOGADOR == 1:
        print('empate')
    elif JOGADOR == 2:
        print('jogador vence')
    else:
        print('jogada INVÁLIDA')
elif computador == 2:
    if JOGADOR == 0:
        print('JOGADOR VENCE')
    elif JOGADOR == 1:
        print('COMPUTADOR VENCE')
    elif JOGADOR == 2:
        print('EMPATE')
    else:
        print('jogada INVÁLIDA')
