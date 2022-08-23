from random import choice

aluno1 = input('Nome do 1 aluno: ')
aluno2 = input('Nome do 2 aluno: ')
aluno3 = input('Nome do 3 aluno: ')
aluno4 = input('Nome do 4 aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]

escolhido = choice(lista)

print(f'O aluno escolhido foi {escolhido} ')
