numeroOperado = int(input('Digite um número: '))
numeroOperado2 = int(input('Digite um 2° número: '))
codigo = int(input('Digite de 1 a 4 para operar os números(1 para a média dos números, 2 para a diferença do maior pro menor, 3 para o produto entre os números e 4 para a divisão do primeiro pelo segundo número): '))

if codigo == 1:
    print((numeroOperado + numeroOperado2) / 2)
elif codigo == 2:
    if numeroOperado > numeroOperado2:
        print(numeroOperado - numeroOperado2)
    if numeroOperado2 > numeroOperado:
        print(numeroOperado2 - numeroOperado)
elif codigo == 3:
    print(numeroOperado * numeroOperado2)
elif codigo == 4:
    print(numeroOperado / numeroOperado2)
else:
    print('Código negado!')