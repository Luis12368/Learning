nome = input('Primeiro nome:')
n_letras = len(nome)

if n_letras <= 4:
    print('Seu nome é curto')
if n_letras == 5 or n_letras == 6:
    print('Seu nome é normal')
if n_letras >= 6:
    print("Seu nome é grande")

"""
Forma correta:

nome = input('Primeiro nome:')
n_letras = len(nome)

if n_letras <= 4:
    print('Seu nome é curto')
elif n_letras <= 6:
    print('Seu nome é normal')
else:
    print("Seu nome é grande")

"""
