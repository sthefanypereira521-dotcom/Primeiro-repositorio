sexo = str(input('informe seu sexo: M/F: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('dados inválidos. por favor, informe novamente: ')
               ).strip().upper()[0]
print(f'seu sexo {sexo} registrado com sucesso!')
