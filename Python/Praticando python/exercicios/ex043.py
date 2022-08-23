peso = float(input('Insira os seu peso: '))
altura = float(input('Insira a sua altura: '))
imc = peso / (altura * altura)

if imc < 18.5:
    print(f'Seu IMC é de {imc:.2f} e você está abaixo do peso.')
elif 18.5 <= imc <= 25:
    print(f'Seu IMC foi de {imc:.2f}, e é o ideal para você.')
elif 25 <= imc <= 30:
    print(f'Seu IMC é de {imc:.2f}, e é sobrepeso.')
elif 30 <= imc <= 40:
    print(f'Seu IMC foi {imc:.2f}, e você está obeso.')
elif imc > 40:
    print(f'Seu imc é de {imc:.2f}, e você esta com Obesidade Morbida')
