n = int(input('Insira um número entre 0 e 20: '))
extenso = ('zero', 'um', 'dois', 'três', 'quatro', ' cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'desseseis', 'dessesete', 'dezoito',
           'dezenove', 'vinte')
while n < 0 or n > 20:
    print('Tente Novamente')
    n = int(input('Insira um número entre 0 e 20: '))
print(f'Você digitou o número {extenso[n]}')
continuar = 'S'
while continuar == 'S':
    continuar = str(input('Deseja continuar S/N? ')).upper().strip()[0]
    if continuar != 'S':
        print('FIM DO PROGRAMA')
        break
    n = int(input('Insira um número entre 0 e 20: '))
    while n < 0 or n > 20:
        print('Tente Novamente')
        n = int(input('Insira um número entre 0 e 20: '))
    print(f'Você digitou o número {extenso[n]}')

