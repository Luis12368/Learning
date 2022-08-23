r1 = float(input('Insira o comprimento da primeira reta:'))
r2 = float(input('Insira o comprimento da segunda reta:'))
r3 = float(input('Insira o coprimento da terceira reta: '))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    if r1 == r2 == r3:
        print(f'O seu triângulo é Equilátero.')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('Seu triangulo é Isósceles')
    else:
        print('Seu triângulo é escaleno.')
else:
    print('Não é possível formar um triângulo com essas retas.')