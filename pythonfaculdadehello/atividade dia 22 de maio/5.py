preco = float(input('Digite um valor: R$'))

if preco <= 50:
    novoPreco = preco * 1.05
elif preco > 50 and preco <= 100:
    novoPreco = preco * 1.10
elif preco > 100:
    novoPreco = preco * 1.15

print('O preço novo é de R${:.2f}'.format(novoPreco))

if novoPreco <= 80:
    print('Barato')
elif novoPreco > 80 and novoPreco <= 120:
    print('Normal')
elif novoPreco > 120 and novoPreco <= 200:
    print('Caro')
elif novoPreco > 200:
    print('Muito Caro')
else:
    print('Erro')
