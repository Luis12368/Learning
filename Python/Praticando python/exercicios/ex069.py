maior_18 = 0
mulher_20 = 0
homens = 0
pessoas = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if sexo == 'F' and idade < 20:
        mulher_20 += 1
    if idade > 18:
        maior_18 += 1
    if sexo == 'M':
        homens += 1
    pessoas += 1
    continuar = str(input('Deseja continuar S/N? ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar S/N? ')).upper().strip()[0]
    if continuar == 'N':
        print(f'Você inseriu {pessoas} pessoas.')
        print(f'''Total de pessoas com mais de 18 anos {maior_18}
Ao todo temos {homens} homens cadastrados
E temos {mulher_20} mulher com menos de 20 anos
''')
        break