n = int(input('Insira um número: '))
print()
print(f'TABUADA DO {n}')
print('-=-' * 5)
for c in range(0, 11):
    print(f'{n}X{c}={c * n}')
print('-=-' * 5)