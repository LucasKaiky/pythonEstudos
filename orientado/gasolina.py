from msilib.schema import Error
from calculadoragasolina import CalculadoraCom
def main():
    print('Os combustíveis são: \nGasolina \nDiesel \nÁlcool')
    try:
        distancia = float(input('Digite a distância: '))
        consumo = float(input('Digite o consumo de combustível do seu veículo [Km/l]: '))
        calc = CalculadoraCom()
        print(calc.calcularGasto(distancia, consumo))
    except:
        print('O valor recebido não é válido')
    
if __name__ == '__main__':
    main()