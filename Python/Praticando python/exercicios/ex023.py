num = int(input('Insira umnúmero de 0 a 9999:'))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print(f'O número {num} tem:')
print(f'{u} Unidades')
print(f'{d} Dezenas')
print(f'{c} Centena')
print(f'{m} Milhar')