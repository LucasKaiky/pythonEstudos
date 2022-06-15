codigoProd = int(input('Digite o código do produto: '))

if codigoProd == 1 or codigoProd == 2:
    print('Sul')
elif codigoProd == 3 or codigoProd == 4:
    print('Sudeste')
elif codigoProd == 5 or codigoProd == 6:
    print('Norte')
elif codigoProd == 7 or codigoProd == 8:
    print('Nordeste')
elif codigoProd == 9 or codigoProd == 10:
    print('Centro-Oeste')
else:
    print('Erro')