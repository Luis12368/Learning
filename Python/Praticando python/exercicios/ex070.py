soma = 0
mais_de_mil = 0
mais_barato = ''
menor = 0
cont = 0
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    soma += preco
    if preco > 1000:
        mais_de_mil += 1
    if cont == 1 or preco < menor:
        menor = preco
        mais_barato = produto
    continuar = str(input('Deseja continuar [S/N]?')).upper()[0]
    if continuar == 'N':
        break
print(f'O total da compra f0i de R${soma}')
print(f'temos {mais_de_mil} produtos custando mais de R$1000')
print(f'O produto mais barato foi {mais_barato} que custa R${menor}')


