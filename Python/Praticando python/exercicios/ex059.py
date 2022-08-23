n1 = float(input('Insira um número: '))
n2 = float(input('Insira um número: '))
opcao = 0
while opcao != 5:
    print('''[1] SOMAR
[2] MULTIPLICAR
[3] MOSTRAR O MAIOR
[4] NOVOS NÚMEROS
[5] SAIR''')
    opcao = int(input('Qual é a sua opcão? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')

    elif opcao == 2:
        mult = n1 * n2
        print(f'O produto entre {n1} e {n2} é {mult}')

    elif opcao == 3:
        maior = n1
        if n2 > maior:
            maior = n2
            print(f'{n2} é maior que {n1}')

        else:
            print(f'{n1} é maior que {n2}')
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Insira um número: '))
        n2 = int(input('Insira mais um valor: '))

    else:
        print('Opção inválida tente novamente.')
print('Programa encerado!, volte sempre.')