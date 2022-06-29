class Calculadora:
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2
    
    def somar(self):
        return self.num1 + self.num2
    def subtrair(self):
        return self.num1 - self.num2
    def dividir(self):
        return self.num1 / self.num2
    def multiplicar(self):
        return self.num1 * self.num2
        
        