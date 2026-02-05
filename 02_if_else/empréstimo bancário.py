casa = float(input('qual o valor da casa?'))
salario = float(input('qual o valor do seu salario?'))
ano = int(input('em quantos anos voçe vai pagar?'))

prestaçao = casa / (ano * 12)
minimo = salario * 30 / 100

print(
    f'para pagar uma casa de R${casa :.2f} em {ano} anos \n '
    f'aprestaçao sera de {prestaçao :.2f}'
)
if prestaçao <= minimo:
    print('emprestimo APROVADO:')
else:
    print('emprestimo NEGADO:')
