peso = float(input('qual é o seu peso? (kg)'))
altura = float(input('qual é a sua altura? (m)'))

imc = peso / (altura ** 2)
print(f'o IMC dessa pessoa é {imc:.2f}')

if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('PESO IDEAL')
elif 25 <= imc < 30:
    print('ESTÁ SOBREPESO')
elif 30 <= imc <= 40:
    print('ESTÁ EM OBESIDADE')
elif imc >= 40:
    print('voçê está em OBESIDADE MÓRBIDA')
