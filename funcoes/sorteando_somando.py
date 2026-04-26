from random import randint
from time import sleep


def sorteia(lista):
    print('=' * 40)
    print('sorteando numeros da lista.')

    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'  {n} ', end=' ', flush=True)

        sleep(0.3)
    print('   CONCLUIDO!')
    print('=' * 40)
    print()
    print()


def somar_par(lista):
    print('=' * 40)
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'somando os numeros pares da lista \n{lista}  \ntemos {soma}.')
    print('=' * 40)


num = list()
sorteia(num)
somar_par(num)
