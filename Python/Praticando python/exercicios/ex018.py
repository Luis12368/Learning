from math import cos, sin, tan, radians

angulo = float(input('Insira o valor do ângulo:'))

radiano = radians(angulo)
seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

print(f'Se o ângulo for {angulo}\no seno sera {seno:.2f}\no cosseno {cosseno:.2f}\ne a tangente {tangente:.2f}')
