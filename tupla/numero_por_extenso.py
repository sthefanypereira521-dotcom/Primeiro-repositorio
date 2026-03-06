cont = ('zero', 'um''dois', 'tres', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez')

while True:
    num = int(input('digite um numero entre 0 e 10: '))
    if 0 <= num <= 10:
        break
    print('tente novamente...', end=' ')
print(f' voce digitou o numero {cont[num]}')
