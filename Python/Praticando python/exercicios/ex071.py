print('=' * 30)
print('{:^40}'.format('BANCO HAUCK'))
print('=' * 30)
valor = int(input('Insira o valor a ser sacado: '))
cedula50 = cedula20 = cedula10 = cedula5 = cedula1 = 0
while True:
    if valor // 50 >= 1:
        cedula50 = valor // 50
        valor = valor - (cedula50 * 50)
        print(f'Total de {cedula50} cédulas de R$50')
    elif valor // 20 >= 1:
        cedula20 = valor // 20
        valor = valor - (cedula20 * 20)
        print(f'Total de {cedula20} cédulas de R$20')
    elif valor // 10 >= 1:
        cedula10 = valor // 10
        valor = valor - (cedula10 * 10)
        print(f'Total de {cedula10} cédulas de R$10')
    elif valor // 5 >= 1:
        cedula5 = valor // 5
        valor = valor - (cedula5 * 5)
        print(f'Total de {cedula5} cédulas de R$5')
    elif valor // 1 >= 1:
        cedula1 = valor // 1
        valor = valor - (cedula1 * 1)
        print(f'Total de {cedula1} cédulas de R$1')
    else:
        break