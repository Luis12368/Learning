valores = list()
while True:
    valores.append(int(input('Insira um número: ')))
    c = str(input('Deseja continuar S/N? ')).upper().strip()[0]
    if c == 'N':
        print(f'Foram digitados {len(valores)} números')
        print(f'A  lista decrescente de números é {sorted(valores, reverse=True)}')
        if 5 in valores:
            print('O número 5 faz parte da lista')
        else:
            print('O número 5 não faz parte da lista')
        break
