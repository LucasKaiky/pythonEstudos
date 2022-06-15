idade = int(input('Digite sua idade(para finalizar o programa digite um número negativo): '))
crianca = 0
adulto = 0

while idade >= 0:
    if idade <= 15:
        crianca += 1
    if idade > 15:
        adulto += 1
    idade = int(input('Digite sua idade(para finalizar o programa digite um número negativo): '))

print('O número de pessoas da 1° faixa etária é {} e o número de pessoas na 2° faixa etária é {}'.format(crianca, adulto))
