valor_inicial = float(input('Insira o valor a ser investido: '))
tempo = int(input('Insira o tempo em anos: '))
r = float(input('Insira a rentabilidade: '))
for c in range(0, tempo):
    valor_ = valor_inicial * (r/100) * tempo
    valor_final = valor_ + valor_inicial
print(f'em {tempo} anos vai render {valor_}, totalizando {valor_final}')