def notas(*n, sit=False):
    """
    ⇒ funcao para analisar notas
    ⇒ *n: uma os mas notas 
    ⇒ sit=True: valor opcional indica se deve ou nao adicionar situacao
    ⇒ return: dicionario com as notas e situacoes(opcional) 
    ⇒ for: opção para percorrer e mostrar cada dado do dicionário separadamente
    """

    notass = dict()

    notass['total'] = len(n)

    notass['maior'] = max(n)

    notass['menor'] = min(n)

    notass['media'] = sum(n)/len(n)

    if sit:
        if notass['media'] >= 7:
            notass['situacao'] = 'boa'
        elif notass['media'] >= 5:
            notass['situacao'] = 'razoavel'
        else:
            notass['situacao'] = 'ta muito ruim'

    return notass


resposta = notas(6.2, 6.8, 3.6, 8.0, sit=True)
print(resposta)

# help(notas)

# for chave, valor  in resposta.items():
# print(chave, valor)
