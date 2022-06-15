produtos = ['pão baguete', 'torrada', 'pão doce', 'café', 'tapioca', 'sonho']
print(produtos)

produto = input('Informe um produto presente na lista(Caso não deseje mais nada digite [parar]): ')
while produto not in (produtos):
    produto = input('Produto inválido! Informe um produto presente na lista(Caso não deseje mais nada digite [parar]): ').strip()

valorTotal = 0

while produto != 'parar':
    quantidade = float(input('Digite a quantidade de produtos que você deseja: '))
    while produto not in (produtos):
        produto = input('Produto inválido! Informe um produto presente na lista(Caso não deseje mais nada digite [parar]): ').strip()

    if produto == 'pão baguete':
        preco = 1.25

    elif produto == 'torrada':
        preco = 4.30

    elif produto == 'pão doce':
        preco = 0.50

    elif produto == 'tapioca':
        preco = 3.50

    elif produto == 'café':
        preco = 1.30

    elif produto == 'sonho':
        preco = 2.35

    if quantidade > 5:
        preco = preco - (preco * 0.10)
        print('Você recebeu um desconto de 10% por ter comprado mais de 5 produtos!!!')

    valorTotal += preco

    print(f'Produto: {produto.capitalize()} \nQuantidade: {quantidade} \nTotal a pagar: R${valorTotal:.2f}')

    produto = input('Informe um produto presente na lista(Caso não deseje mais nada digite [parar]): ')

print(f'O valor total foi de R$ {valorTotal:.2f}')