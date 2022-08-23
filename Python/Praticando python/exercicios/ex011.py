altura = float(input('Insira a altura da parede: '))
base = float(input('Insira a base da parede: '))

area = base * altura
tinta = area / 2

print(f'Será preciso {tinta:.2f} litros de tinta,\npara pintar uma parde com {area:.2f}m²')