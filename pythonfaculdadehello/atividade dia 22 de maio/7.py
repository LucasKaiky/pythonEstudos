atleta = ''
while True:
    atleta = input('Digite o nome do atleta: ')
    distancia = float(input('Digite a distância pecorrida em metros: '))
    tempo = int(input('Digite o tempo até o fim do percurso: '))
    velocidade = distancia / tempo
    print('A velocidade do atleta {} é de {} m/s'.format(atleta, velocidade))
    
    continuar = input('Deseja continuar? [sim/nao]: ')
    
    if continuar == "nao":
        break

