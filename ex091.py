from random import randint
from time import sleep

jogo = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}

print('Valores sorteados: ')
for k,v in jogo.items():
    print(f'O {k} tirou {v}')
print('--'*20)

c = 1
print('Ranking dos jogadores: ')
for item in sorted(jogo, key = jogo.get, reverse= True):
    print(f'\t=> {c}° lugar: {item} tirou {jogo[item]}')
    sleep(1)
    c += 1
