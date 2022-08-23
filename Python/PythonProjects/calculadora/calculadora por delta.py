

import math


a = int(input("Insira A:"))
b = int(input("Insira B:"))
c = int(input("Insira C:"))

delta = b * b - 4 * a * c

if delta < 0:
    print("A equação não possui números reais")

elif delta == 0:
    raiz = -b / (2 * a)
    print(f"Delta =0  Resulta em X1 = {raiz}")

elif delta > 0:
    raiz_1 = (-b + math.sqrt(delta)) / (2*a)
    raiz_2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Resulta em X1 = {raiz_1} e X2 = {raiz_2}")


