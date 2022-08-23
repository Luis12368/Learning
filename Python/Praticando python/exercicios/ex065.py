soma = 0
cont = 0
controlador = 'S'
maior = menor = 0
while controlador == 'S':
    n = int(input('Insira um número: '))

    if controlador == 'S':
        controlador = str(input('Deseja continuar S/N?')).upper()
        cont += 1
        soma += n
        if cont == 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
media = soma / cont
print(f'Você digitou {cont} números e a média foi {media}')
print(f'O maior número digitado foi {maior}, o menor {menor}')
