'''Faça um programa para uma padaria utilizando lista:
Receba um produto por vez e a quantidade dele
O usuário deve informar quando não quiser comprar mais nada
Calcule o valor total e apresente a lista de produtos e quantidades compradas
Se ele tiver comprado mais de 5 unidades de um produto, deve receber um desconto de 10% nele (e ser avisado sobre isso)
PRODUTOS:
Pão baguete - R$1,25 Torrada - R$ 4,3
Pão doce - R$0,50 Café - R$1,30
Tapioca - R$3,50 Sonho - R$ 2,35'''

produtos = ['pão baguete', 'torrada', 'pão doce', 'café', 'tapioca', 'sonho']
print (produtos)

produto = input('Informe um produto presente na lista(Caso não deseje mais nada digite [parar]): ')
while produto not in (produtos):
    produto = input('Produto inválido! Informe um produto presente na lista(Caso não deseje mais nada digite [parar]): ')
quantidade = float(input('Digite a quantidade de produtos que você deseja: '))
preco = 0
precoTotal = 0
while produto != 'parar':
    
    if produto == 'pão baguete':
        preco = 1.25
        if quantidade > 5:
            preco = preco - (preco * 0.10)
            print('Você recebeu um desconto de 10% por ter comprado mais de 5 produtos!!!')
        print(f'Produto: Pão Baguete \nQuantidade: {quantidade} \nTotal a pagar: R${preco * quantidade :.2f}')
    elif produto == 'torrada':
        preco = 4.30
        if quantidade > 5:
            preco = preco - (preco * 0.10)
            print('Você recebeu um desconto de 10% por ter comprado mais de 5 produtos!!!')
        print(f'Produto: Torrada \nQuantidade: {quantidade} \nTotal a pagar: R${preco * quantidade :.2f}')
        
    elif produto == 'pão doce':
        preco = 0.50
        if quantidade > 5:
            preco = preco - (preco * 0.10)
            print('Você recebeu um desconto de 10% por ter comprado mais de 5 produtos!!!')
        print(f'Produto: Pão Doce \nQuantidade: {quantidade} \nTotal a pagar: R${preco * quantidade :.2f}')
        
    elif produto == 'tapioca':
        preco = 3.50
        if quantidade > 5:
            preco = preco - (preco * 0.10)
            print('Você recebeu um desconto de 10% por ter comprado mais de 5 produtos!!!')
        print(f'Produto: Tapioca \nQuantidade: {quantidade} \nTotal a pagar: R${preco * quantidade :.2f}')
        
    elif produto == 'café':
        preco = 1.30
        if quantidade > 5:
            preco = preco - (preco * 0.10)
            print('Você recebeu um desconto de 10% por ter comprado mais de 5 produtos!!!')
        print(f'Produto: Café \nQuantidade: {quantidade} \nTotal a pagar: R${preco * quantidade :.2f}')
        
    elif produto == 'sonho':
        preco = 2.35
        if quantidade > 5:
            preco = preco - (preco * 0.10)
            print('Você recebeu um desconto de 10% por ter comprado mais de 5 produtos!!!')
        print(f'Produto: Sonho \nQuantidade: {quantidade} \nTotal a pagar: R${preco * quantidade :.2f}')

    precoTotal += preco * quantidade
    produto = input('Informe um produto presente na lista(Caso não deseje mais nada digite [parar]): ')
    if produto != 'parar':
        quantidade = int(input('Digite a quantidade de produtos que você deseja: '))
        
print(f'O valor total a ser pago é de R${precoTotal :.2f}')