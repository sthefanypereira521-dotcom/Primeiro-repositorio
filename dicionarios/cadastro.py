from datetime import datetime

dados = dict()
dados['nome'] = str(input('nome:'))
nascimento = int(input('ano de nascimento:'))
dados['idade'] = datetime.now().year - nascimento
dados['sexo'] = str(input('sexo [M/F]: ')).upper()
dados['ctps'] = int(input('numero da carteira de trabalho (0 NÃO TEM): '))

if dados['ctps'] != 0:
    dados['contrataçao'] = int(input('ano da contrataçao: '))
    dados['salario'] = float(input('salario: R$'))

if dados['sexo'] == 'F':
    idade_min = 60
else:
    idade_min = 65


dados['aposentadoria'] = idade_min

print('-=-' * 15)
for k, v in dados.items():
    print(f' - {k} => {v}')
