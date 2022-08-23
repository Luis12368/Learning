algo = input("Insira algo:")
print('O tipo primitivo desse valor é', type(algo))
print('Só tem espaços?', algo.isspace())
print('É um número?', algo.isalnum())
print('É alfabetico?', algo.isalpha())
print('É alfanumerico?', algo.isalnum())
print('Está em maiúscula?', algo.isupper())
print('Está em miniscula?', algo.islower())
print('Está capitalizada?', algo.istitle())  # primeira letra maiúscula
