produtoCaro = 0
for x in range(1,11):
    preco = float(input('Digite o valor do produto: R$'))
    if preco > produtoCaro:
        produtoCaro = preco
print('O produto mais caro é de R${:.2f}'.format(produtoCaro))