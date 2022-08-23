from datetime import datetime

nascimento = int(input('Insira seu ano de nascimento: '))
idade = datetime.today().year - nascimento

if idade < 18:
    print('Você ainda vai se alistar')
    tempo = 18 - idade
    print(f'Falta {tempo} anos para você se alistar')
elif idade == 18:
    print('Está na hora de você se alistar')
else:
    print('Já passou da hora de se alistar')
    tempo = idade - 18
    print(f'Já passou {tempo} desde que vc se alistou')