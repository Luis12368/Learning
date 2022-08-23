n = float(input('Insira uma nota: '))
n2 = float(input('Insira mais uma: '))
m = (n + n2)/2
print(f'Tirando {n} e {n2} a média do aluno é {m}')
if m < 5:
    print('Reprovado')
elif 5 <= m < 7:
    print('Você ficou em recuperação')
else:
    print('Você foi aprovado.')
