"""
nome = input('Qual é o seu nome?')
idade = int(input('Qual é a sua idade?'))
idade_menor = 18
idade_maior = 50

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} voc~e pode fazer o emprestimo')
else:
    print(f'{nome} NÃO pode fazer o emprestimo')
"""
nome = input('Qual o seu nome?')
idade = int(input("Qual a sua idade?"))
ano_de_nascimento = 2022-idade

if ano_de_nascimento == 2003:
    print(f'Você tem direito as ferias.')
else:
    print('Você não tem direito as ferias')