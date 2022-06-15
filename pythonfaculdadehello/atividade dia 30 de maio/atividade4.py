numeros = []
somaPositivos = quantNegativos = 0

for c in range(4):
    numeros.append(float(input('Digite um valor: ')))

for numero in numeros:
    if numero > 0:
        somaPositivos += numero
    if numero < 0:
        quantNegativos += 1

print(f'Quantidade de numeros negativos: {quantNegativos}\nSoma dos numeros positivos: {somaPositivos}')