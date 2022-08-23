import time
from random import choice
from time import sleep
print('-=-' * 12)
print('Bem vindo ao jogo!')
print('-=-' * 12)

player1 = str(input('Escolha entre, Pedra, Papel ou Tesoura: ')).upper()
escolha = 'PEDRA', 'PAPEL', 'TESOURA'
player2 = choice(escolha)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!!')
print('-=-' * 11)
print(f'COMPUTADOR JOGOU {player2}')
print(f'JOGADOR JOGOU {player1}')
print('-=-' * 11)

if player1 == 'PEDRA' and player2 == 'TESOURA':
    print('Você ganhou!')
    print(f'{player1} ganha de {player2}')
elif player1 == 'TESOURA' and player2 == 'PAPEL':
    print('Você ganhou!')
    print(f'{player1} ganha de {player2}')
elif player1 == 'PAPEL' and player2 == 'PEDRA':
    print('Você ganhou!')
    print(f'{player1} ganha de {player2}')
elif player1 == player2:
    print('Deu empate')
else:
    print(f'Você perdeu, {player2} ganha de {player1}')
