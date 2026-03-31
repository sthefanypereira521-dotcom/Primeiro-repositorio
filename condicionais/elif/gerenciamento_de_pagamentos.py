print('\033[31m' + f'{" LOJAS RAINHA ":=^40}' + '\033[m')
preço = float(input('preço das compras: R$ '))

print(f''' \033[32m {"FORMAS DE PAGAMENTOS"} \033[m
[ 1 ]  á vista dinheiro/cheque   
[ 2 ]  á vista cartão
[ 3 ]  2x no cartão 
[ 4 ]  3x ou mais no cartão''')

opção = int(input('qual é a opção?'))

if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalPARC = int(input('quantas parcelas? '))
    parcela = total / totalPARC
    print(
        f'sua compra será parcelada em {totalPARC}x de R${parcela:.2f} COM JUROS')
else:
    total = 0
    print(' OPÇÃO INVÁLIDA ')
print(f'sua compra de R${preço:.2f} vai custar R${total:.2f} no final')
