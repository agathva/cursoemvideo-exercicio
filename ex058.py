from random import randint
from time import sleep


print('Vou pensar em um número entre 0 e 10 e você tentará adivinhar')
print('Pensando em um número...')
comp = randint(1, 10)
sleep(2)
jogador = int(input('Em que numero pensei? '))
palpite = 1
print('--'*30)

while comp != jogador:
    if jogador > comp:
        jogador = int(input('Menos... Qual seu palpite? '))
    else:
        jogador = int(input('Mais... Qual seu palpite? '))
    palpite += 1

print('=='*30)
print(f'PARABÉNS! Acertou na {palpite}° tentativa.')
