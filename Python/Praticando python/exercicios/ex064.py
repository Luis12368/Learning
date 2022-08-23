cont = 0
n = 0
soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999:
        soma += n
        cont += 1
    else:
        print(f'Você digitou {cont} números, e a soma deles é {soma}')
