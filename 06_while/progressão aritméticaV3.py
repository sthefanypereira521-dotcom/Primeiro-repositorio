primeiro = int(input('primeiro termo: '))
razão = int(input('razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('quantos termos voçê quer mostrar a mais aqui? '))
print(
    f'-=-=-=- FIM -=-=-=- \nprogressão aritmética finalizada com {total} termos mostrados:')
