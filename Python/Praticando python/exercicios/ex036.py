valor = float(input('Insira o valor da casa:'))
salario = float(input('Insira o valor do seu sálario:'))
anos = float(input('Insira em quantos anos você pretende pagar:'))

parcela = valor / (anos * 12)
sla = salario * 0.30
if parcela < sla:
    print('Você irá poder fazer o empréstimo.')
    print(f'E irá pagar uma mensalidade de R${parcela:.2f} por {anos} anos')
else:
    print('Infelizmente você não pode fazer o empréstimo')