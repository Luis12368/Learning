nome = input('Insira o nome d euma cidade:')
nome_novo = nome.upper().split()

if nome_novo[0] == 'SANTOS':
    print('A cidade começa com o nome Santos.')

else:
    print(f'A cidade de {nome}, não começa o nome  Santos ')
