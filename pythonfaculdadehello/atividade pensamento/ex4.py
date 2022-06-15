'''04
– Em uma eleição presidencial existem quatro
candidatos. Os votos são informados por meio de código.
Os códigos utilizados são: 1, 2, 3, 4

-Votos para os respectivos candidatos 
(você deve montar a tabela 
ex: 
1-Jose/ 2-João/etc
5-Voto Nulo
6-Voto em Branco

• Faça um programa que calcule e mostre: O total de votos
para cada candidato; O total de votos nulos; O total de
votos em branco; A percentagem de votos nulos sobre o
total de votos; A percentagem de votos em branco sobre o
total de votos.
• Para finalizar o conjunto de votos tem-se o valor zero..'''

votos = []

print('''    1 - José
    2 - João
    3 - Luiz
    4 - Lucas
    5 - Voto Nulo
    6 - Voto em Branco''')
while True:
    voto = int(input('''Digite o seu voto: '''))
    while voto not in [0, 1, 2, 3, 4, 5, 6]:
        voto = int(input('''Codigo inválido! Digite o seu voto: '''))
    if voto == 0:
        break
    votos.append(voto)

quantidadeVotos1 = votos.count(1)
quantidadeVotos2 = votos.count(2)
quantidadeVotos3 = votos.count(3)
quantidadeVotos4 = votos.count(4)
quantidadeVotos5 = votos.count(5)
quantidadeVotos6 = votos.count(6)

totalVotos = len(votos)
print(f'{totalVotos} Pessoas votaram neste turno!')
print(f'Total de votos em José: {quantidadeVotos1} ({quantidadeVotos1*100/totalVotos:.2}%)')
print(f'Total de votos João: {quantidadeVotos2} ({quantidadeVotos2*100/totalVotos:.2}%)')
print(f'Total de votos Luiz: {quantidadeVotos3} ({quantidadeVotos3*100/totalVotos:.2}%)')
print(f'Total de votos Lucas: {quantidadeVotos4} ({quantidadeVotos4*100/totalVotos:.2}%)')
print(f'Total de votos Nulos: {quantidadeVotos5} ({quantidadeVotos5*100/totalVotos:.2}%)')
print(f'Total de votos em Branco: {quantidadeVotos6} ({quantidadeVotos6*100/totalVotos:.2}%)')