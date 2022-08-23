print("------Conversor de medidas------\n")

valor = float(input("Insira o valor em graus celsius: "))

F = valor * 1.8 + 32
F = ("{:.2f}". format(F))

print(f'{valor} graus Celsius sõa iguais a {F}, graus Fahrenheit')