from random import randint
computador = randint(0, 10)

print('aqui é o computador pensei em um número entre 0 e 10')
print('será que voçe acerta qual foi? ')
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('qual seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('mais...')
        elif jogador > computador:
            print('menos...')
print(f'acertou com {palpites}:PARABÉNS ')
