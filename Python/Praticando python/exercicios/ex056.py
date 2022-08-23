mulher_menor = 0
s_idade = 0
maior = 0
menor = 0
nome_ = ''
for c in range(1, 5):
    print(f'----- {c} PESSOA -----')
    nome = str(input('Insira seu nome:'))
    idade = int(input('Insira sua idade: '))
    sexo = str(input('[M/F]')).upper()
    s_idade = idade + s_idade
    if sexo == 'F':
        if idade < 20:
            mulher_menor = mulher_menor + 1
    elif sexo == 'M':
        if c == 1:
            maior = idade
            menor = idade
            nome_ = nome

        else:
            if idade > maior:
                maior = idade
                nome_ = nome
media_idade = s_idade / 4
print(f'Tem {mulher_menor} mulheres com a idade abaixo dos 20.')
print(f'O homem mais velho é {nome_} com {maior} anos')
print(f'A idade média é {media_idade}')