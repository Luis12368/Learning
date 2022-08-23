times = ('Palmeiras', 'Corinthians', 'Athletico-PR', 'Internacional', 'Atlético-MG',
         'Fluminense', 'Santos', 'São Paulo', 'Flamengo', 'Botafogo', 'Avaí', 'Bragantino', 'Atlético-GO',
         'Goiás', 'Ceará', 'Coritiba', 'América-MG', 'Cuiabá', 'Juventude', 'Fortaleza')
print('-=-' * 50)
print(f'Lista de times do brasileirão: {times}')
print('-=-' * 50)
print('Os 5 primeiros colocados no brasileirão são:')
print('-=-' * 20)
for posicao in range(0, 5):
    print(f'O {posicao+1} colocado no campeonato Brasileiro é {times[posicao]}')
print('-=-' * 20)
print(f'Os últimos 4 times do brasileirão são:')
print('-=-' * 20)
for posicao in range(16, 20):
    print(f'O {posicao+1} colocado no campeonato é o {times[posicao]}')
print('-=-' * 20)
print(f'Os ordem dos times em ordem afabetica é:')
print('-=-' * 20)
print(sorted(times))
print('-=-' * 20)
print(f'O flamengo está na {times.index("Flamengo")+1} posição do braileirão')
