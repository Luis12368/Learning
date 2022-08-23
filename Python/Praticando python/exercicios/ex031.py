d = float(input('Insira distancia ser percorrida: '))
if d <= 200:
    p = d * 0.50
    print(f'A viagem vai custar R${p:.2f}')
else:
    p = d * 0.45
    print(f'A viagem vai custar R${p:.2f}')