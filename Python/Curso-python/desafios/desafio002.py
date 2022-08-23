horario_1 = input('Digite seu horário:')

if horario_1.isdigit():
    horario_1 = int(horario_1)
    if horario_1 < 0 or horario_1 > 23:
        print('Horário deve estar entre 0 e 23')

    else:
       if horario_1 <= 11:
        print('Bom dia')
       elif horario_1 <= 17:
        print('Boa tarde')
       else:
        print('Boa noite')
else:
    print('insira um numero inteiro')


