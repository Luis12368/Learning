from math import hypot
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))

hipotenusa = hypot(co, ca)

print(f'O comprimento da hipotenusa será: {hipotenusa:.2f}')
