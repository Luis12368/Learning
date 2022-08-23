print('-' * 36)
print('Calcule o custo do horário do futebol')
print('-' * 36)

v = float(input('Insira o preço por hora: '))
horas = float(input('Insira o tempo jogado: '))
n_jogadores = int(input('Insira o número de jogadores: '))
valor = v * horas
valor_pesso = valor / n_jogadores
print(f'Se o horário custar {v:.2f} e for jogado por {horas} hora, o custo é de R${valor:.2f}.')
print(f'E se o valor for dividido em {n_jogadores} pessoas, será R${valor_pesso} para cada.')