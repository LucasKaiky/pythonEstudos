codigo = int(input('Digite um número para o código de 1 a 4(se o 0 for digitado a operação finalizará): '))

while codigo != 0:
    quantidade = int(input('Digite a quantidade que deseja: '))
    if codigo == 1:
        print('Caderno - R$12.00')
        valor = 12.00
    if codigo == 2:
        print('Régua - R$2.50')
        valor = 2.50
    if codigo == 3:
        print('Borracha - R$0.25')
        valor = 0.25
    if codigo == 4:
        print('Mochila - R$50.00')
        valor = 50.00
    total = valor * quantidade
    print('O valor total é de R${}'.format(total))
    codigo = int(input('Digite um número para o código de 1 a 4(se o 0 for digitado a operação finalizará): '))
