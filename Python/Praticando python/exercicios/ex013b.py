valor = float(input('Insira o valor do produto: '))

desconto = float(input('Insira o vlaor do desconto: '))

novo_valor = valor - (valor * (desconto / 100))

print(f'O novo valor com {desconto}% de desconto é {novo_valor:.2f}')
