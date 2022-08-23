conjunto = {1, 2, 3, 4, 5}
print("Conjunto 1 = ", conjunto)
conjunto_2 = {5, 6, 7, 8, 9}
print("Conjunto 2 = ", conjunto_2)
conjunto_uniao = conjunto.union(conjunto_2) #faz a união
print("união: {}".format(conjunto_uniao))
conjunto_intersection = conjunto.intersection(conjunto_2) #faz a intersecção
print("intersecção: {}".format(conjunto_intersection))
conjunto_diferenca = conjunto.difference(conjunto_2)#mostra a diferença dos itens
print("Diferença entre 1 e 2 : {}".format(conjunto_diferenca))
conjunto_diferenca_2 = conjunto_2.difference(conjunto)
print("Diferença entre 1 e 2 : {}".format(conjunto_diferenca_2))
#conjunto = {1, 2, 3, 4, 5}
# conjunto.add(6) adciona
# conjunto.discard(2) remove
# print(conjunto)