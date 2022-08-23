ficha = []

while True:
    nome = str(input('Insira seu nome: '))
    nota1 = float(input('Insira a 1o nota: '))
    nota2 = float(input('Insira a 2o nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja coninuar? [S/N]'))
    if resp in 'Nn':
        print(ficha)
        break
print('-_-' * 10)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print("-" * 30)
    opc = int(input('Mostrar a nota de qual aluno?(999 interrompe): '))
    if opc == 999:
        print('FINALIZANDO')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]}  são {ficha[opc][1]}')