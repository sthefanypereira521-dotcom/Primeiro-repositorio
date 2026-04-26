from time import sleep


def contador(ini, fim, pas):
    texo = f'contagem de {ini} ate {fim} em passo {pas} '
    tam = len(texo) + 4

    print('~' * tam)
    print(texo)
    print('~' * tam)

    sleep(2.2)

    if ini < fim:
        cont = ini
        while cont <= fim:
            print(f'{cont}', end=' ⇒ ', flush=True)
            sleep(0.4)
            cont += pas
        print('FIM\n')

    else:
        cont = ini
        while cont >= fim:
            print(f'{cont}', end=' ⇒ ', flush=True)
            sleep(0.4)
            cont -= pas
        print('FIM\n')


print()
contador(1, 10, 1,)
contador(10, 0, 2)
