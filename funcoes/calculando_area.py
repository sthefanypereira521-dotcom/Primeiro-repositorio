def área(lar, comp):
    a = lar * comp
    print(f'área do terreno {lar} x {comp} e de {a}m² ')


print('-=-' * 14)
print('              area de terreno             ')
print('-=-' * 14)

l = float(input('largura (M): '))
c = float(input('comprimento (M):'))
área(l, c)
