from random import randint
from time import sleep

print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
comp = randint(0, 5)
print('-=-'*20)
sleep(2)
jogador = int(input('Em que numero pensei? '))

if comp == jogador:
    print(f'PARABÉNS! Você conseguiu me vencer {comp}')
else:
    print(f'GANHEI! Eu pensei em {comp} e você pensou em {jogador}')
print('-=-'*20)
