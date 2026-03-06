palavras = ('aprender', 'algoritmo', 'python', 'git', 'http', 'apirest',
            'bancos de dados', 'frameworks', 'autenticacao',
            'seguranca', 'testes', 'futura', 'programadora', 'backend')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
