produto = float(input('Insira o valor so produto R$: '))
print("""Digite:
1 Para pagamento a vista em dinheiro/cheque.
2 Para pagamento a vista no cartão.
3 Para pagamento parcelado no cartão(Juros de 20%).""")
m_pagamento = int(input('Qual opção?'))

if m_pagamento == 1:
    produto = produto - (produto * 0.10)
    print(f'Você recebeu um desconto de 10% e vai pagar R${produto:.2f}.')
elif m_pagamento == 2:
    produto = produto - (produto * 0.05)
    print(f'Você recebeu um desconto de 5%, e ira pagar R${produto:.2f}.')
elif m_pagamento == 3:
    vezes = int(input('Insira o número de vezes a ser parcelado: '))
    parcela = produto / vezes
    if vezes <= 2:
        print(f'Você não teve desconto e irá pagar 2 parcelas de R${parcela:2f}.')
    else:
        produto = produto + (produto * 0.20)
        parcela = produto / vezes
        print(f'Você parcelou em {vezes} vezes,totalizando R${produto}, com o valor da parcela de R${parcela:.2f}.')