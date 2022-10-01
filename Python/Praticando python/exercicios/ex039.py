from datetime import datetime

nascimento =  int(input('Ano de nascimento: '))
idade = datetime.today().year -  nascimento

if idade < 18:
    print(f'Você ainda não se alistou.')
    print(f'{18 - idade} anos para se alistar')
elif idade == 18:
    print('Está na hora de se alistar')
else:
    print('Já passou da hora de se alistar')
    print(f'Faz {idade - 18} que você se alistou.')