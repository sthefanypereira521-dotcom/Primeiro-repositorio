def aumentar(preco=0, taxa=0, format=False):
    """
    Aumenta o valor de um preço com base em uma porcentagem.
    format=False: se True, retorna valor formatado em moeda.
    Retorno: valor aumentado, formatado ou não.

    """

    resp = preco + (preco * taxa / 100)
    return resp if format is False else moeda(resp)


def diminuir(preco=0, taxa=0, format=False):
    resp = preco - (preco * taxa/100)
    return resp if format is False else moeda(resp)


def dobro(preco=0, format=False):
    resp = preco * 2
    return resp if format is False else moeda(resp)


def metade(preco=0, format=False):
    resp = preco / 2
    return resp if format is False else moeda(resp)


def moeda(preco=0, moeda='R$'):
    """
    Formata: um valor numérico para moeda.
    Retorno: valor formatado em moeda.

    """

    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, taxa_aum=10, taxa_red=5):
    print('~' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('~' * 35)
    print(f'preco analisado: \t{moeda(preco)}')
    print(f'dobro do preco:  \t{dobro(preco, True)}')
    print(f'metade do preco: \t{metade(preco, True)}')
    print(f'{taxa_aum}% de aumento: \t{aumentar(preco, taxa_aum, True)}')
    print(f'{taxa_red}% de reduçao:   \t{diminuir(preco, taxa_red, True)}')
    print('~' * 35)
