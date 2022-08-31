horario = float(input('Insira o seu horário: '))

if 0 <= horario <= 11:
    print('Bom dia')
elif 12 <= horario <= 17:
    print('Boa tarde')
elif 18 <= horario <= 23:
    print('Boa noite')