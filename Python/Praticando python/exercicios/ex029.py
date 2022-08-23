velocidade = float(input('Insira velocidade do seu carro:'))
limite = 80
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você passou do limite de velocidade!')
    print(f'E sua multa será de R${multa:.2f}')

