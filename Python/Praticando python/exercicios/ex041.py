from datetime import datetime
ano = int(input('Insira o seu ano de nascimento: '))
idade = datetime.today().year - ano
if idade <= 9:
    print('Você é mirim')
elif idade <= 14:
    print('Você é Infantil')
elif idade <= 19:
    print('Você é junior')
elif idade <= 25:
    print('Você é sênior: ')
else:
    print('Você é master')