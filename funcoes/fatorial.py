from time import sleep


def fatorial(n, show=False):
    """
    ⇒ calcula o fatorial de um numero.
    ⇒ show=True: (opcional) de mostrar conta 
    ⇒ flush=True: exibe cada numero imediatamente durante a impressão.
    """
    f = 1
    for c in range(n, 0, -1):
        sleep(0.5)
        if show:
            print(c, end=' ', flush=True)
            if c > 1:
                print(f'x', end=' ')
            else:
                print('=', end=' ')
        f *= c
    return f


# help(fatorial)
print(fatorial(6, show=True))
