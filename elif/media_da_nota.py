nota1 = float(input('primeira nota:'))
nota2 = float(input('segunda nota:'))
media = (nota1 + nota2)/2

if 7 > media >= 5:
    print('RECUPERAÇAO')
elif media  < 5:
    print('REPROVADO:')
elif media >= 7:
    print('APROVADO:')
    