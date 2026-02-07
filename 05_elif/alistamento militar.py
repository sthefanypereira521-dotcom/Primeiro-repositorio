from datetime import date

atual = date.today().year
nasc = int(input('em que ano voçe nasceu?'))
idade = atual - nasc

if idade == 18:
    print('ja e hora de se alistar:')
elif idade < 18:
    saldo = 18 - idade
    print(f'ainda vai se alistar , faltam  anos {saldo} para o alistamento')
elif idade > 18:
    saldo = idade - 18
    print(f'passou do tempo deveria ter se alistado há  anos {saldo} ')
