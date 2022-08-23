lista = ('Caneta', 2.0, 'Borracha', 0.75, 'Livro', 10.0,
         'Caderno', 15.90, 'Mochila', 90.60)
print('-' * 40)
print('{:^40}'.format('LISTAGEM DE PREÇO'))
print('-' * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>2.2f}')
