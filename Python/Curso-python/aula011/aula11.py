"""
and, or, not
in e not in

"""
usuario = input('Nome de usuario:')
senha = input('Insira sua senha:')

senha_db = '12345'
usuario_db = 'luis'

if usuario_db == usuario and senha_db == senha:
    print('Você está logado')
else:
    print("senha ou usuaário inválido")

