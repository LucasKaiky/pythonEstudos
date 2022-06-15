'''Exercicio 033
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Dicas: Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro; Triângulo Equilátero: três lados iguais; Triângulo Isósceles: quaisquer dois lados iguais; Triângulo Escaleno: três lados diferentes;'''
lados = []

for x in range(1,4):
    lado = int(input('Digite o valor dos lados do triângulo: '))
    lados.append(lado) 
    
if lados[0] == lados[1] == lados [2]:
    print('Triângulo Equilátero')         
elif lados[0] == lados[1] != lados[2] or lados[1] == lados[2] != lados[0] or lados[0] == lados[2] != lados[1]:
    print('Triângulo Isóceles')
else:
    print('Triângulo Escaleno')
