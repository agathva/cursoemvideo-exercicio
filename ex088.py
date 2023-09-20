from random import randint
from time import sleep


palpites = list()
numeros = list()
print('-='*25)
print(f'{"JOGA NA MEGA SENA":^45}')
print('-='*25)

jogos = int(input('Quantos jogos voce quer que eu sorteie: '))
for i in range(0, jogos):
    for j in range(0, 6):
        x = randint(1, 60)
        numeros.append(x)
    palpites.append(numeros[:])
    numeros.clear()

for i in range(0, jogos):
    print(f'Jogo {i+1}: {palpites[i]}')
    sleep(1)
print(f'{"BOA SORTE":-^50}')
