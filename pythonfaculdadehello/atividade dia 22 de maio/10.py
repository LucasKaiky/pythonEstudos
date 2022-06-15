idade = int(input('Digite sua idade(Digite um número negativo para finalizar): '))
adolescente = 0

while idade >= 0:
    if idade >= 12 and idade <= 17:
        adolescente += 1
    idade = int(input('Digite sua idade(Digite um número negativo para finalizar): '))

print('A quantidade de adolescentes é {}'.format(adolescente))
