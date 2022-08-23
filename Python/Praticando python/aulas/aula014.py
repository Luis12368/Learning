nome = str(input('Insira o seu nome: ')).upper()
if nome == 'LUIS':
    print('Que nome bonito!')
elif nome == 'MARIA' or 'PEDRO' or 'PAULO':
    print('Seu nome é bastante usado no Brasil')
else:
    print(f'Prazer em te conhecer {nome}, tenha um bom dia!')