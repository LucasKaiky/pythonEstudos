compras = []
produtoAbaixo = 0
produtoEntre = 0
produtoAcima = 0

for x in range(1,6):
    preco = float(input('Digite o valor do produto: '))
    compras.append(preco)

for produtos in compras:
    if produtos < 50:
        produtoAbaixo += 1
    if produtos >= 50 and produtos <= 80:
        produtoEntre += 1
    if produtos > 80:
        produtoAcima += 1

mediaPrecos = sum(compras) / len(compras)
print (f'A quantidade de produtos abaixo de R$50.00 é de: {produtoAbaixo} \nA quantidade de produtos entre R$50.00 e R$80.00 é de: {produtoEntre} \nA quantidade de produtos acima de R$80.00 é de: {produtoAcima} \nE a média de preço dos produtos é de {mediaPrecos}')
    