n1 = int(input('Insira um número: '))
n2 = int(input('Insira mais um número: '))
soma = n1 + n2
mult = n1 * n2
div = n1 / n2
div2 = n1 // n2
e = n1 ** n2

print(f'A soma entre {n1} e {n2} é {soma},o prooduto {mult}, e a divisão {div:.3f}', end=' ')
print(f'Divisão inteira {div2} e potência {e}')

