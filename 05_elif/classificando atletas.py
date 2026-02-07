from datetime import date
atual = date.today().year

nasc = int(input('em que ano voçê nasceu?'))
idade = atual - nasc

print(f'o atleta tem {idade} anos')

if idade <= 9:
    print('atleta MIRIM')
elif idade <= 14:
    print('atleta INFANTIL ')
elif idade <= 19:
    print('atleta JUNIOR')
elif idade <= 25:
    print('atleta SêNIOR')
elif idade > 25:
    print('atleta MASTER')
