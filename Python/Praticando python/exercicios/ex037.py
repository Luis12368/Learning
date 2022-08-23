num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] Converter para Binário.
[2] Converter para Octal.
[3] Converter para Hexadecimal''')
opcao = int(input('escolha a sua opção: '))

if opcao == 1:
    print(f'{num} Convertido para binário é igual a:{bin(num)[2:]} ')
elif opcao == 2:
    print(f'{num} Convertido para octal é igual a:{oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} Convertido para hexadecimal é igual a: {hex(num)[2:]} ')
else:
    print('Opção inválida')