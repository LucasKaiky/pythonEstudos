class CalculadoraCom:
    def __init__(self):
        self.valorGasolina = 7.25
        self.valorDiesel = 7.50
        self.valorAlcool = 5.00

    def calcularGasto(self, distancia, consumo):
        if (distancia <= 0 or consumo <= 0):
            raise Exception('o valor recebido não pode ser menor ou igual a zero')

        gastoGasolina = round((distancia / consumo) * self.valorGasolina, 2)
        gastoDiesel = round((distancia / consumo) * self.valorDiesel, 2)
        gastoAlcool = round((distancia / consumo) * self.valorAlcool, 2)

        return f'''O valor total será de: 
        Gasolina: R${gastoGasolina}
        Diesel: R${gastoDiesel}
        Álcool: R${gastoAlcool}'''

