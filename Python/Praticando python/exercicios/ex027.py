nome = str(input('Insira o seu nome completo:')).strip()
nome = nome.split()
print('Seu primeiro nome é', nome[0])
print('Seu sobre nome é', nome[len(nome)-1])
