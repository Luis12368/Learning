from random import randint
from time import sleep
palpites = []
print('-' * 30)
print('{:^30}'. format('JOGO NA MEGA SENA'))
print('-' * 30)
q = int(input('Insira o número de palpites: '))
for c in range(0, q):
    cont = 0
    while True:
        n = randint(0, 60)
        if n not in palpites:
            palpites.append(n)
            cont += 1
        if cont >= 6:
            print(sorted(palpites))
            sleep(0.5)
            palpites.clear()
            break
