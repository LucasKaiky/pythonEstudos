import numpy as np
salarios = []
filhos = []
nomes = []

while True:
    salario = float(input('Digite seu salário(para finalizar digite um número negativo): R$'))
    if salario < 0:
        break
    salarios.append(salario)
    nomes.append(str(input('Digite seu nome: ')))
    filhos.append(int(input('Digite o número de filhos: ')))
    
mediaSalario = sum(salarios) / len(salarios)
mediaFilhos = sum(filhos) / len(filhos)

np_salario = np.array(salarios)
np_salario = np_salario[np_salario<1500]
porcentagem = len(np_salario) * 100 / len(salarios)
salarios.sort()
print(f'''A média salarial é de R${mediaSalario}
      A média de filhos é de {mediaFilhos}
      A pessoa mais rica é: {nomes[salarios.index(max(salarios))]}
      A pessoa mais pobre é: {nomes[salarios.index(min(salarios))]}
      A porcentagem de pessoas com menos de R$1500 salarial é {porcentagem}''')

    
    