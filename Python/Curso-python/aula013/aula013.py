num1 = input('Insira um número: ')
num2 = input('Insira mais um número: ')

try:  # isdigit verifica se a string pode ser convertida em inteiro
    num1 = float(num1)
    num2 = float(num2)
    print(num1 + num2)

except:
    print('ERROR')
