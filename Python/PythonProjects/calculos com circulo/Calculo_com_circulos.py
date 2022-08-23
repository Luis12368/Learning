raio = input('Digite o raio(número inteiros):')

if raio.isdigit():
    pi = 3.14159265359
    raio = int(raio)
    diametro = 2 * raio
    perimetro = diametro * pi
    perimetro = ("{:.2f}".format(perimetro))
    area = pi * raio **2
    area = ("{:.2f}".format(area))
    print(f'Se o raio for {raio}, o diâmetro vai ser {diametro}, a area {area} e o perimetro {perimetro}')

else:
    print('Digite um número inteiro')
