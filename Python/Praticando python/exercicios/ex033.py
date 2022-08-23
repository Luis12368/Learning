a = float(input('Insira um número: '))
b = float(input('Insira mais um: '))
c = float(input('Insira mais um: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor número é {menor}')
print(f'O menor número será {maior}')
