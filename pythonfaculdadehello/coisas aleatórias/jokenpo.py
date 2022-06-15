import random 
from time import sleep


def jokenpo():
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('POO!!!')


jogadas = ['PEDRA', 'PAPEL', 'TESOURA']
score = 0
resposta = 'sim'
jogador = str(input('PEDRA , PAPEL ou TESOURA? ')).strip().upper()
bot = str(random.choice(jogadas))

while True:
    jokenpo()
    print(f'O computador jogou: {bot}')
    print(f'O jogador jogou: {jogador}')
    if bot == 'PEDRA':
        if jogador == 'TESOURA':
            print('Você perdeu!!!')
        elif jogador == 'PAPEL':
            print('Você ganhou!!! PARABÉNS!!!')
            score += 1
        elif jogador == 'PEDRA':
            print('EMPATE!')
        else:
            print('RESPOSTA INVÁLIDA!')

    if bot == 'TESOURA':
        if jogador == 'PAPEL':
            print('Você perdeu!!!')
        elif jogador == 'PEDRA':
            print('Você ganhou!!! PARABÉNS!!!')
            score += 1
        elif jogador == 'TESOURA':
            print('EMPATE!')
        else:
            print('RESPOSTA INVÁLIDA!')

    elif bot == 'PAPEL':
        if jogador == 'PEDRA':
            print('Você perdeu!!!')
        elif jogador == 'TESOURA':
            print('Você ganhou!!! PARABÉNS!!!')
            score += 1
        elif jogador == 'PAPEL':
            print('EMPATE!')
        else:
            print('RESPOSTA INVÁLIDA!')
    resposta = str(input('Deseja jogar novamente [sim / não]? '))
    if resposta != 'sim':
        break
    
    jogador = str(input('PEDRA , PAPEL ou TESOURA? ')).strip().upper()
    bot = str(random.choice(jogadas))

print(f'Sua pontuação foi de {score} vitórias!')
