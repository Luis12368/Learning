n = int(input('Insira uma nota: '))
n2 = int(input('Insira a segunda nota: '))
m = (n + n2)/2
print(f'Sua média foi {m}')
if m >= 6:
    print(f'Sua média foi boa!')
else:
    print('Sua notafoi baixa, ESTUDE mais!')