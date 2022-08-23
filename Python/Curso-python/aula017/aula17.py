contador = 1
acumulador = 2

while contador <= 20:

    print(contador, acumulador)

    if contador > 18:
        break

    contador = contador + 1
    acumulador = acumulador + contador
else:
    print('O código encerrou')

