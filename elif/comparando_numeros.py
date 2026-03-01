n1 = int(input('digite um numero:'))
n2 = int(input('digite outro numero:'))

if n1 > n2:
    print(f' o primeiro valor e MAIOR {n1}')
elif n2 > n1:
    print(f'o segundo valor e MAIOR {n2}')
else:
    print(f'nao existe maior valor , os 2 sao iguais {n1} e {n2}')
