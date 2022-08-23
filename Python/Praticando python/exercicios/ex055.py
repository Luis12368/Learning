maior = 0
menor = 0
for p in range(0, 5):
    peso = float(input('Insira o seu peso:'))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f'O menor peso é {menor}, e o maior {maior} ')
