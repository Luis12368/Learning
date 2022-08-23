matriz = []
for c in range(0, 3):
    n = int(input(f'Insira um número para posição {0},{c}: '))
    matriz.append(n)
for c in range(0, 3):
    n = int(input(f'Insira um número para posição {1},{c}: '))
    matriz.append(n)
for c in range(0, 3):
    n = int(input(f'Insira um número para posição {2},{c}: '))
    matriz.append(n)
for c in range(0, 3):
    print(f'[{matriz[c]}]', end='   ')
print()
for c in range(3, 6):
    print(f'[{matriz[c]}]', end='   ')
print()
for c in range(6, 9):
    print(f'[{matriz[c]}]', end='   ')

# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# for l in range(0, 3):
#   for c in range(0, 3)
#       matriz[l][c] = int(input('Insira um número: '))
# print('-=-' * 30)
# for l in range(0, 3):
#   for c in range(0,3):
#       print(f'{matriz[l][c]:^5}', and='')









