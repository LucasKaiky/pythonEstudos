from calculadora123 import Calculadora
num1 = float(input('Digite o 1° número: '))
metodo = str(input('Digite um método [* | / | - | +]: '))
num2 = float(input('Digite o 2° número: '))
calc = Calculadora(num1,num2)
if metodo == '+':
    print(f'A soma entre os números é: {calc.somar()}')
elif metodo == '-':
    print(f'A subtração entre os números é: {calc.subtrair()}')
elif metodo == '/':
    print(f'A divisão entre os números é: {calc.dividir()}')
elif metodo == '*':
    print(f'A multiplicação entre os números é: {calc.multiplicar()}')