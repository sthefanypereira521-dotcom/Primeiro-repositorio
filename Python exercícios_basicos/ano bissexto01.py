ano = int(input('que ano analisar?'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano {} e BISSEXTO'.format(ano))
else:
    print('o ano {} NAO e BISSEXTO'.format(ano))
