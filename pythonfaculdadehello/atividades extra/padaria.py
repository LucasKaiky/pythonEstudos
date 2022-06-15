'''Faça um programa para uma padaria utilizando lista:
Receba um produto por vez e a quantidade dele
O usuário deve informar quando não quiser comprar mais nada
Calcule o valor total e apresente a lista de produtos e quantidades compradas
Se ele tiver comprado mais de 5 unidades de um produto, deve receber um desconto de 10% nele (e ser avisado sobre isso)
PRODUTOS:
Pão baguete - R$1,25 Torrada - R$ 4,3
Pão doce - R$0,50 Café - R$1,30
Tapioca - R$3,50 Sonho - R$ 2,35'''
def desconto(quantidade, preco, produtos):
    if quantidade > 5:
        preco = preco - (preco * 0.1)
        print('Você recebeu um desconto de 10% por ter comprado mais de 5 produtos!!!')
    print(f'Produto: {produtos} \nQuantidade: {quantidade} \nTotal a pagar: R${preco * quantidade :.2f}')


produtos = ['pão baguete', 'torrada', 'pão doce', 'café', 'tapioca', 'sonho']
print(produtos)

produto = input('Informe um produto presente na lista(Caso não deseje mais nada digite [parar]): ')
while produto not in (produtos):
    produto = input('Produto inválido! Informe um produto presente na lista(Caso não deseje mais nada digite [parar]): ')
quantidade = float(input('Digite a quantidade de produtos que você deseja: '))
preco = 0

while produto != 'parar':

    if produto == 'pão baguete':
        desconto(quantidade, 1.25, produtos[0])
    if produto == 'torrada':
        desconto(quantidade, 4.30, produtos[1])
    if produto == 'pão doce':
        desconto(quantidade, 0.5, produtos[2])
    if produto == 'café':
        desconto(quantidade, 1.3, produtos[3])
    if produto == 'tapioca':
        desconto(quantidade, 3.5, produtos[4])
    if produto == 'sonho':
        desconto(quantidade, 2.35, produtos[5])

    produto = input('Informe um produto presente na lista(Caso não deseje mais nada digite [parar]): ')
    if produto != 'parar':
        quantidade = int(input('Digite a quantidade de produtos que você deseja: '))