valores = list()
val_max = 0
val_min = 0
for c in range(0, 5):
    valores.append(int(input(f'Insira um número  para posição {c}: ')))
    if c == 0:
        val_min = val_max = valores[c]
    else:
        if valores[c] > val_max:
            val_max = valores[c]
        if valores[c] < val_min:
            val_min = valores[c]
print(f'Você digitou os valores {valores}')
print(f'\nO maior número digitado foi {val_max} nas posições', end='')
for i, v in enumerate(valores):
    if v == val_max:
        print(f' {i}...', end='')
print(f'\nO menor valor digitado foi {val_min}, nas posições', end='')
for i, v in enumerate(valores):
    if v == val_min:
        print(f' {i}...', end='')
