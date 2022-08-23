from random import randint
n = (randint(0, 10), randint(0, 10), randint(0, 10),
     randint(0, 10), randint(0, 10))
print(f'Os valores sorteados são: {n}')
print(f'O menor número é {min(n)}')
print(f'O maior número é {max(n)}')