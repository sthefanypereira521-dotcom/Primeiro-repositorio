from random import randint
computador = randint(0,5)
print('-=-' * 20) 
print('vou pensar em um numero entre 0 e 5 . tente adivinhar ....')
print('-=-' * 20)
jogador = int(input('em que numero eu pensei ?')) 
if jogador == computador:
    print('parabens voçe conseguiu')
else:
    print('ganhei!!! eu pensei no  {} e nao no  {}: '.format(computador,jogador))
