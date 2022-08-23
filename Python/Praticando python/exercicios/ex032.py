a = int(input('Insira um ano: '))
if a % 4 == 0:
    if a % 100 == 0 and a % 400 ==0:
        print(f'{a} é um ano bissexto')
    else:
        print(f'{a} Não é um ano bissexto')
else:
    print(f'{a} não é um ano bissexto')
