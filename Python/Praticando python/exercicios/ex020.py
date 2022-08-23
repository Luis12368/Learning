from random import shuffle

aluno1 = input('Insira um nome: ')
aluno2 = input('Insira mais um nome: ')
aluno3 = input('Insira mais um nome: ')
aluno4 = input('Insira mais um nome: ')

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print(f'Os escolhidos foram:')
print(lista)
