from datetime import datetime

pessoa = {}
pessoa['nome'] = input('Insira seu nome: ')
pessoa['nascimento'] = int(input('Ano de nascimento: '))
pessoa['sexo'] = str(input('Sexo M/F: ')).upper().strip()
pessoa['carteira'] = int(input('Carteira de trabalho (0 não tem): '))
data_atual = datetime.today().year
if pessoa['carteira'] != 0:
    pessoa['contratação'] = int(input('Insira o ano de contratção: '))
    pessoa['salario'] = int(input('Sálario: R$'))
    pessoa['idade'] = data_atual - pessoa['nascimento']
    pessoa['aposentadoria'] = pessoa['contratação'] + 35 - pessoa['nascimento']
print('-=-' * 20)
for k, v in pessoa.items():
    print(f' {k} tem valor {v}')