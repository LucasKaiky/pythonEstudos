salario = float(input('Digite seu salário: R$'))

if salario < 300:
    print('O salário reajustado é de R${}'.format(salario * 1.45))
elif salario >= 300 and salario <= 600:
    print('O salário reajustado é de R${}'.format(salario * 1.25))
elif salario > 600:
    print('O salário reajustado é de R${}'.format(salario * 1.15))
else:
    print('Erro')