dias = float(input('quantos dias alugados?: '))
km = float(input('Quantos Km rodaodos?: '))

custo = (km * 0.15) + (dias * 60)

print(f'O total a pagar é de R${custo:.2f}')
