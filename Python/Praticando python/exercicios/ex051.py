termo = int(input('Insira o primeiro termo: '))
razao = int(input('Insira a razão: '))
ultimo = termo + (10 - 1) * razao
for c in range(termo, ultimo + razao, razao):
    print(c)
