aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))

print(f'Nome é igual a {aluno["Nome"]} ')
print(f'Média é igual a {aluno["Média"]}')
if aluno["Média"] >= 7:
    print(f'Situaçõa igual a aprovado.')
else:
    print('Situação igual a reprovado.')
