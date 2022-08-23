frase = 'Curso em vídeo'
#        01234567891011121314 indice
print(frase)
print(frase[3])  # [3] Representa o indice que começa por 0
print(frase[:13])  # [:13] Indice vai do 0 a 13
print(frase[1:15:2])  # Vai do indice 0 ao 15 pulando de 2 em 2

print(frase.count('o'))
print(frase.replace('Curso', 'Alemão'))  # Substitui curso por alemão temporariamente