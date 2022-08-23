while True:
    print()
    numero_1 = input('Digite um número:')
    numero_2 = input("Digite um número:")
    operador_1 = input("Digite o operador(+,-,* ou /):")
    sair = input('Para sair digite [s]im e [n] para não ')
    if sair == 's':
        break
    if not numero_1.isnumeric() or not numero_2.isnumeric():
        print('Digite um número ')
        continue

    numero_2 = int(numero_2)
    numero_1 = int(numero_1)

    if operador_1 == '+':
        print(numero_1 + numero_2)
    elif operador_1 == '-' :
        print(numero_1 - numero_2)
    elif operador_1 == '*':
        print(numero_1 * numero_2)
    elif operador_1 == '/':
        print(numero_1 / numero_2)
    else:
        print('Operador invalido')



