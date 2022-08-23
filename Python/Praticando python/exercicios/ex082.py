valores = list()
pares = list()
impares = list()
while True:
    n = int(input('Insira um valor: '))
    valores.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    c = str(input('Deseja continuar S/N? ')).upper().strip()[0]
    if c == 'N':
        print(f'Os valores digitados foram {valores}')
        print(f'Os valores pares digitados foram {pares}')
        print(f'Os valores impares digitados foram {impares}')
