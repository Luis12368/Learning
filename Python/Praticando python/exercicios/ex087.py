matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = []
coluna3 = []
linha2 = []
for linha in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Insira um número para posição {linha},{c}: '))
        matriz[linha][c] = n
        if n % 2 == 0:
            pares.append(n)
        if c == 2:
            coluna3.append(n)
        if linha == 1:
            linha2.append(n)
for linha in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[linha][c]:^5}]', end='')
    print()

print(f'A soma dos valores pares é {sum(pares)}')
print(f'A soma dos valores da terceira coluna é {sum(coluna3)}')
print(f'O maior número da segunda linha é {max(linha2)}')