n = int(input('Insira um número: '))
s = 0
for c in range(1, n + 1):
    if n % c == 0:
        s = s + 1
if s > 2:
    print(f'O número {n} não é primo')
else:
    print(f'O número {n} é primo')