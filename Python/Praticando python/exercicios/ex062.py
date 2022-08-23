termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
cont = 0
while cont < 10:
    termo += razao
    cont += 1
    print(termo)
r = str(input('Quer ver mais termos? digite S/N ')).upper()
while r == 'S':
    mais_termos = int(input('Quantos termos quer ver?'))
    cont = 0
    if mais_termos > 0:
        while cont < mais_termos:
            termo += razao
            cont += 1
            print(termo)
    else:
        print('Você acrescentou 0 termos')
else:
    print('FIM')