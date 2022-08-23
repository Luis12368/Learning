num = int(input("insira um número:"))
div = 0
for x in range(1, num+1):
    resto = num % x
    if resto == 0:
        div += 1
if div == 2:
    print(f"O número {num} é primo.")
else:
    print(f"O número {num} não é primo.")
