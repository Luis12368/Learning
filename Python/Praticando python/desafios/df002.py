#Você terá o desafio de ler um valor inteiro, que é o tempo 
#de duração em segundos de um determinado evento em uma loja,
#e informe-o expresso no formato horas:minutos:segundos.
segundos = int(input("Insira a quantidade de segundos: "))

minutos = int(segundos/60)#TODO Implementar a formula para calcular os minutos.
segundos = int(segundos - (minutos * 60))
horas = int(minutos/60) #TODO Implementar a formula para calcular as horas.
minutos = int(minutos - (horas * 60))

print("{}:{}:{}".format(horas, minutos, segundos))