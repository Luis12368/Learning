valor_produto = float(input('Insira o valor do produto: '))

desconto = valor_produto * 0.05
novo_valor = valor_produto - desconto

print(f'Com um desconto de 5% o produto vai custar {novo_valor:.2f} Reais')
