def calculadora():
    numero1 = float(input('Digite o 1° número: '))
    numero2 = float(input('Digite o 2° número: '))
    resultado = 0
    simbolo = str(input('Diga qual operação você deseja [+] [-] [/] [*]:  '))
    if simbolo == '+':
        resultado = numero1 + numero2
    if simbolo == '-':
        resultado = numero1 - numero2
    if simbolo == '/':
        resultado = numero1 / numero2
    if simbolo == '*':
        resultado = numero1 * numero2
    return(resultado)
    
calculo = calculadora()

print(calculo)
