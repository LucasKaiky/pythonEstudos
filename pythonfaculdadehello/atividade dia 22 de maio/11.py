gosta = 0
naoGosta = 0
for x in range(1,16):
    beterraba = int(input('Você gosta de beterraba(Digite 1 para [Sim} e 2 para [Não])? '))
    while beterraba < 1 or beterraba > 2:
        beterraba = int(input('NÚMERO INVALIDO! Você gosta de beterraba(Digite 1 para [Sim} e 2 para [Não])? '))
    if beterraba == 1:
        gosta += 1
    if beterraba == 2:
        naoGosta += 1
    
print('A quantidade de pessoas que gostam de beterraba é de {} e a quantidade que não gosta é de {}'.format(gosta, naoGosta))
