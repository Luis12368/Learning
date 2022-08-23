from datetime import date
d_maior = 0
for c in range(1, 8):
    ano = int(input('Insira o seu ano de nascimento:'))
    idade = date.today().year - ano
    if idade >= 21:
        d_maior = d_maior + 1
d_menor = 7 - d_maior
print(f'Neses grupo de pessoas {d_maior} atingiram a maioridade e {d_menor} não.')