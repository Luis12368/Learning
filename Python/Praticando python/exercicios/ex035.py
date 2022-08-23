r1 = float(input('Insira o valor de uma reta:'))
r2 = float(input('insira mais um valor:'))
r3 = float(input('E mais um:'))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('è possível formar um triângulo com essas retas')
else:
    print('Não é possível formar um triãngulo com essas retas.')