num = (int(input('Insira um número: ')),
       int(input('Insira mais um número: ')),
       int(input('Insira mais um número:')),
       int(input('E mais um número: ')))
print(f'O número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O número 3 apareceu pela primeira vez na {num.index(3) + 1} posição')
else:
    print('O valor 3 não foi digitao nenhuma vez')
print('Os valores pares digitados foram: ')
for n in num:
    if n % 2 == 0:
        print(n)
