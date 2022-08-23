class calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def subtracao(self):
        return self.valor_a - self.valor_b

    def soma(self):
        return self.valor_a + self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

if __name__=='__main__':
    calculadora = calculadora(10, 2)

    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.divisao())
    print(calculadora.multiplicacao())

