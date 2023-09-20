jogador = dict()
gol = list()

jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
partida = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, partida):
    gol.append(int(input(f'Quantos gols na {c+1}° partida? ')))
jogador['gols'] = gol[:]
jogador['total'] = sum(gol)
print('-='*30)
print(jogador)

print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('-='*30)
print(f'O jagador {jogador["nome"]} jogou {partida} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'\t =>Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
