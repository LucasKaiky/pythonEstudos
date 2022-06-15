import random 
from time import sleep

def jokenpo():
    print('\033[1;35mJO\033[m')
    sleep(0.5)
    print('\033[1;35mKEN\033[m')
    sleep(0.5)
    print('\033[1;35mPOO!!!\033[m')


jogadas = ['PEDRA', 'PAPEL', 'TESOURA']
score = 0
resposta = 'sim'
jogador = str(input('PEDRA , PAPEL ou TESOURA? ')).strip().upper()
bot = str(random.choice(jogadas))

while True:
    while jogador not in jogadas:
        jogador = str(input('JOGADA NEGADA!!! PEDRA , PAPEL ou TESOURA? ')).strip().upper()
    ('giorno.mp3')
    jokenpo()
    print('=-=' * 10)
    print(f'\033[1;36mO computador jogou: {bot}\033[m')
    print(f'\033[1;36mO jogador jogou: {jogador}\033[m')
    if bot == 'PEDRA':
        if jogador == 'TESOURA':
            print('\033[1;31mVocê perdeu!!!\033[m')
        elif jogador == 'PAPEL':
            print('\033[1;32mVocê ganhou!!! PARABÉNS!!!\033[m')
            score += 1
        elif jogador == 'PEDRA':
            print('EMPATE!')
        else:
            print('RESPOSTA INVÁLIDA!')

    elif bot == 'TESOURA':
        if jogador == 'PAPEL':
            print('\033[1;31mVocê perdeu!!!\033[m')
        elif jogador == 'PEDRA':
            print('\033[1;32mVocê ganhou!!! PARABÉNS!!!\033[m')
            score += 1
        elif jogador == 'TESOURA':
            print('EMPATE!')
        else:
            print('RESPOSTA INVÁLIDA!')

    elif bot == 'PAPEL':
        if jogador == 'PEDRA':
            print('\033[1;31mVocê perdeu!!!\033[m')
        elif jogador == 'TESOURA':
            print('\033[1;32mVocê ganhou!!! PARABÉNS!!!\033[m')
            score += 1
        elif jogador == 'PAPEL':
            print('EMPATE!')
        else:
            print('RESPOSTA INVÁLIDA!')
            
    print('=-=' * 10)
    resposta = str(input('\033[1;33mDeseja jogar novamente [sim / não]? \033[m')).strip().lower()
    if resposta != 'sim':
        break
    
    jogador = str(input('PEDRA , PAPEL ou TESOURA? ')).strip().upper()
    bot = str(random.choice(jogadas))

print(f'Sua pontuação foi de {score} vitória(s)!')