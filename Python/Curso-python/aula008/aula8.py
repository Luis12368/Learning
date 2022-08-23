"""
numero_1 = input('Digite um número: ') #iput sempre irá retornar sting
numero_2 = input('Digite outro número: ')

print(int(numero_1) + int(numero_2))

nome = input('Qual é o seu nome?')
print(f'olá {nome}, tudo bem? ')
tudo_bem = input()
"""
nome = input('qual o seu nome? ')
idade = input('quantos anos você tem? ')
#ano_de_nascimento = 2022-idade(errado porque idade virou uma str, e 2022 é inteiro)
ano_de_nascimento = 2022-int(idade)#maneira certa.
print()
print(f'{nome} nasceu em {ano_de_nascimento} e tem {idade} anos')