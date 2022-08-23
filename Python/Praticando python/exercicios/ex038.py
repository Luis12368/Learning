n = float(input('Insira um número: '))
n2 = float(input('Insira mais um: '))

if n > n2:
    print('O primeiro valor é maior')
elif n2 > n:
    print('O segundo valor é o maior')
else:
    print('Não existe valor maior, os dois números são iguais.')