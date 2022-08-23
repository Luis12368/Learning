s = float(input('Insira o seu sálario: '))

if s > 1250:
    s = (s * 0.10) + s
    print(f'Seu sálario com aumento de 10% será R${s:.2f}')
else:
    s = (s * 0.15) + s
    print(f'Seu sálario com aumento de 15% será R${s:.2f}')