nome = 'Luis'
peso = 85
altura = 1.87
ano_atual = 2021
idade = 18
nascimento = ano_atual - idade
imc = peso/altura**2

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'o IMC de {nome} é {imc:.2f}')
print(f'{nome} nasceu em {nascimento}')