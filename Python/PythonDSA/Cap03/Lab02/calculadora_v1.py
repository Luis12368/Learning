# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")
print("""Selecione a opção:
1-Soma
2-Subtração
3-Multiplicação
4-Divisão
""")
op = int(input('Digite a opção desejada: '))
num1 = int(input('Insira um número: '))
num2 = int(input('Insira mais um: '))

if op == 1:
    print(f'{num1} + {num2} =', num1+num2)
elif op == 2:
    print(f'{num1} - {num2} =', num1-num2)
elif op == 3:
    print(f'{num1} * {num2} =', num1*num2)
elif op == 4:
    print(f'{num1}  / {num2} =', num1/num2)
else:
    print('Digite um número válido')


