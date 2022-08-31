num = input('Digite um número: ')

try:
    if num % 2 == 0:
        print('O número é par')
    else:
        print('O número é impar')

except:
    print('Digite um número válido')
