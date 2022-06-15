for x in range(1,10):
    numero = int(input('Digite um número: '))
    print(numero * 3)
    if (numero < 0):
        print('É negativo')
    elif (numero > 0):
        print('É positivo')
    else:
        print('Número é zero')
