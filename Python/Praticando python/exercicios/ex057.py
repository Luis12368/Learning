genero = str(input('Insira [M]para masculino e [F] para feminino: ')).strip().upper()[0]
while genero != 'M' and genero != 'F':
    print('Dados inválidos')
    genero = str(input('Insira M ou F:')).upper()
print(f'Sexo {genero} registrado com sucesso.')