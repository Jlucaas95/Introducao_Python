class Calculadora:

     def soma(self, valor_a, valor_b):
        return  valor_a + valor_b

     def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

     def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

     def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()

print(calculadora.soma(10, 5))
print(calculadora.subtracao(15, 5))
print(calculadora.multiplicacao(5, 8))
print(calculadora.divisao(10, 2))
