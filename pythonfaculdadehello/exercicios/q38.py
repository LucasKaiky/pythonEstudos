'''Faça um Programa para um caixa eletrônico.

O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.

As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.

O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.'''

saque = int(input('Digite o valor do saque(valor mínimo é de: R$10 / valor máximo é de: R$600): R$'))
while saque < 10 or saque > 600:
        saque = int(input('Valor inválido!!! Digite o valor do saque(valor mínimo é de: R$10 / valor máximo é de: R$600): R$'))
        

if saque >= 10 and saque <= 600:  
    notas100 = notas50 = notas10 = notas5 = notas1 = 0
    notas100, saque = divmod(saque,100)
    notas50, saque = divmod(saque,50)
    notas10, saque = divmod(saque,10)
    notas5, saque = divmod(saque,5)
    notas1, saque = divmod(saque,1)

    if notas100 > 0:
        print(f'{notas100} nota(s) de R$100')
    if notas50 > 0:
        print(f'{notas50} nota(s) de R$50')
    if notas10 > 0:
        print(f'{notas10} nota(s) de R$10')
    if notas5 > 0:
        print(f'{notas5} nota(s) de R$5')
    if notas1 > 0:
        print(f'{notas1} nota(s) de R$1')
    


    

