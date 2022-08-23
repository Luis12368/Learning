cont = 0
n = int(input('Quer ver a tabuda de qual valor? '))
print('-' * 20)
print(f'Tabuada do {n}')
print('-' * 20)
while True:
    if n < 0:
        print('Você digitou um número inválido!')
        break
    print(f'{cont}X{n}={cont*n}')
    cont += 1
    if cont > 10:
        n = int(input('Quer ver a tabuda de qual valor? '))
        cont = 0

