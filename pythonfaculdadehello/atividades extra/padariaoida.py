produtos = ["pão baguete",
            "torrada",
            "pão doce",
            "café",
            "tapioca",
            "sonho"]
precos = [1.25, 4.30, 0.5, 1.3, 3.5, 2.35]
quantidades = [0,0,0,0,0,0]
resposta = "sim"
valor_total = 0
while (resposta != "não"):
    produto = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade: "))
    indice = produtos.index(produto)
    quantidades[indice] = quantidade
    resposta = input("Consumiu mais algum produto? ")
    while (resposta != "sim" and resposta != "não"):
        print("Informação inválida! "
              "Digite sim ou não")
        resposta = input("Consumiu mais algum produto?")
else:
    print("COMANDA: ")

print("Você comprou: ")

for i in range(len(quantidades)):
    preco_produto = 0.0
    if(quantidades[i] > 0):
        if(quantidades[i] > 5):
            preco_produto = 0.9 * precos[i]
        else:
            preco_produto = precos[i]
    valor = quantidades[i] * preco_produto
    print(produtos[i], "-", quantidades[i],
          "--> valor = R$", valor)
    valor_total += valor

print("O valor total é R$", valor_total)