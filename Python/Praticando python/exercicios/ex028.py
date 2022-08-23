from random import randint

print('-=-' * 11)
print('Bem-vindo ao jogo da adivinhação')
print('-=-' * 11)
print('Em que número eu pensei?!')
n = int(input('Escolha um número entre 0 e 10: '))
numero_secreto = randint(0, 5)
if n == numero_secreto:
    print('Parabéns você acertou')
else:
    print('Que pena você errou :(')
