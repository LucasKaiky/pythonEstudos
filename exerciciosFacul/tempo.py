def calculoVar ():
    variacaoDis = float(input('Distância final(KM): ')) - float(input('Distância inicial(KM): '))
    variacaoTemp = float(input('Tempo pecorrido(horas): ')) - float(input('Tempo iniciado(horas): '))
    calculoVariacao = variacaoDis / variacaoTemp
    return (calculoVariacao)

media = calculoVar()

print(f'A velocidade média é: {media :.2f}Km/h')
