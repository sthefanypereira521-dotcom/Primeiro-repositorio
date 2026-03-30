from random import randint
from time import sleep
lista = list()
jogos = list()

print('-=-' * 15)
print('                   mega sena                ')
print('-=-' * 15)

quantos = int(input(' quantos jogos voce quer que eu sorteio?\n '))
total = 1
while total <= quantos:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('-=-' * 5, f'SORTEANDO {quantos} JOGOS', '-=-' * 5, '\n')
for i, lista in enumerate(jogos):
    print(f'jogo {i+1}:{lista}')
    sleep(1)
print('-=-' * 5,  ' BOA SORTE ', '-=-' * 5)
