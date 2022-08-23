lista = list()
while True:
    n = int(input('Insira um número: '))
    if n not in lista:
        print('Valor adcionado com sucesso!')
        lista.append(n)
    else:
        print('Valor duplicado não vou adcionar')
    c = str(input('Deseja continuar S/N? ')).upper().strip()[0]
    if c == 'N':
        print(f'Os valores digitados foram {sorted(lista)}')
        break
