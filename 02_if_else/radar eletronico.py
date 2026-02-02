velocidade = float (input('qual e a velocidade atual do seu carro? '))
if velocidade > 70:
    print('MULTADO voce ultrapassou o limite que e de 70km/h')
    multa = (velocidade - 70) * 7
    print('voce deve pagar uma multa de R${:.2f}'.format(multa))
print('tenha um otimo dia com segurança')
