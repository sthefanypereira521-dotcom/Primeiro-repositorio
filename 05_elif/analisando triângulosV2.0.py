r1 = float(input('primeiro segmento: '))
r2 = float(input(' segundo segmento: '))
r3 = float(input('terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos acima podem FORMAR um TRIÂNGULO:')
    if r1 == r2 == r3:
        print('triângulo EQUILATERO')
    elif r1 != r2 != r3 != r1:
        print('triângulo ESCALENO')
    else:
        print('triângulo ISÓSCELES')
else:
    print('os segmentos acimas  NAO PODEM FORMAR TRIÂNGULOS:')
