otimo = 0
bom = 0
regular = 0
for x in range(1,16):
    opiniao = int(input('Qual foi sua opinião sobre o filme? Digite 1 para regular, 2 para bom e 3 para ótimo:'))
    while opiniao < 1 or opiniao > 3:
        opiniao = int(input('NÚMERO INVÁLIDO!!! Qual foi sua opinião sobre o filme? Digite 1 para regular, 2 para bom e 3 para ótimo:'))
    if opiniao == 1:
        regular += 1
    if opiniao == 2:
        bom += 1
    if opiniao == 3:
        otimo += 1

print('O número de pessoas que acharam o filme regular foi {}, o número de pessoas que acharam o filme bom foi {} e o número de pessoas que acharam o filme ótimo foi {}'.format(regular, bom, otimo))