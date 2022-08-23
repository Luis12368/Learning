from random import randint
jogador = str(input('Escolha Impar ou Par: ')).strip().upper()
while jogador not in 'IMPARPAR':
    jogador = str(input('Escolha Impar ou Par: ')).strip().upper()
n = int(input('Escolha um número de 0 a 9: '))
while jogador not in 'IMPARPAR' or n < 0:
    n = int(input('Escolha um número de 0 a 9: '))
cont = 0
pc_escolhe = 'IMPAR'
while jogador not in 'IMPARPAR' or n < 0:

    n = int(input('Escolha um número de 0 a 9: '))
while True:
    pc = int(randint(0, 10))
    soma = n + pc
    if jogador == 'IMPAR':
        pc_escolhe = 'PAR'
    if jogador == 'PAR':
        pc_escolhe = 'IMPAR'
    if soma % 2 == 0 and jogador == 'PAR':
        cont += 1
        print('Parabens você ganhou!!!')
        print(f'Você escolheu {jogador}, e o PC {pc_escolhe}')
        print(f'A soma entre {n} e {pc} é {soma}  e esse valor é PAR')
        print(f'Você ganhou {cont} vezes')
        print()
        jogador = str(input('Escolha Impar ou Par: ')).strip().upper()
        n = int(input('Escolha um número de 0 a 9: '))
    elif soma % 2 != 0 and jogador == 'IMPAR':
        cont += 1
        print('Parabens você ganhou!!!')
        print(f'Você escolheu {jogador}, e o PC {pc_escolhe}')
        print(f'A soma entre {n} e {pc} é {soma}  e esse valor é IMPAR')
        print(f'Você ganhou {cont} vezes')
        print()
        jogador = str(input('Escolha Impar ou Par: ')).strip().upper()
        n = int(input('Escolha um número de 0 a 9: '))
    else:
        print('Você perdeu :(')
        print(f'Você escolheu {jogador}, e o PC {pc_escolhe}')
        print(f'A soma entre {n} e {pc} é {soma} {pc_escolhe}')
        break
