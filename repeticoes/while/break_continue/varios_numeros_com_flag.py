n = s = 0
cont = 0

while True:
    n = int(input('digite um numero: (999 PRA PARAR!) '))
    if n == 999:
        break
    cont += 1
    s += n
print(f'a soma vale {s}')
print(f' foram digitados {cont} numeros ')
