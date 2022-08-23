from random import randint

print('-=-' * 11)
print('Bem vindo ao jogo da adivinhação!!!')
print('-=-' * 11)
print('Insira um valor de 0 a 10')
print()
tentativas = 0
numero_secreto = randint(0, 10)
numero = 0

while numero != numero_secreto:
    numero = int(input('insira um número: '))
    print(numero_secreto)

    if numero == numero_secreto:
        print('Parabéns você ganhou!!!')

    elif numero != numero_secreto:
        if numero > numero_secreto:
            print(f'Menos... Tente novamente')
            tentativas += 1
        elif numero < numero_secreto:
            print(f'Mais... Tente novamente')
            tentativas += 1
print(f'E seu número de tentativas foi de {tentativas}')
