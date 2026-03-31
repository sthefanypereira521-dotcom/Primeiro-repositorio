from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for pess in range(1, 6):
    nasc = int(input(f'em que ano a {pess}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f' tivemos o total de {totmaior} pessoas maiores de idade. ')
print(f' e tivemos o total de {totmenor} pessoas menores idade. ')
