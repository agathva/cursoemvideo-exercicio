time = list()
jogadores = dict()
gol = list()

while True:
    jogadores.clear()
    gol.clear()
    jogadores['nome'] = str(input('Nome do jogador: ')).strip().title()
    partida = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))
    for c in range(0, partida):
        gol.append(int(input(f'Quantos gols na {c + 1}° partida? ')))
    jogadores['gols'] = gol[:]
    jogadores['total'] = sum(gol)
    time.append(jogadores.copy())
    while True:
        resp = str(input('Deseja continuar? (S/N) ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N')
    if resp in 'N':
        break
    print('-=' * 30)

print('-='*30)
print(f'{"COD"} {"NOME":<15}{"GOLS":<15}{"TOTAL":<15}')
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print("-="*30)
while True:
    while True:
        cod = int(input('Mostrar dados de qual jogador? [999 INTERROMPE] '))
        if 0 <= cod < len(time) or cod == 999:
            break
        print(f"ERRO! Não existe jogador com o código {cod}")
    if cod == 999:
        break
    print(f"-- LEVANTAMENTO DO JOGADOR {time[cod]['nome']}")
    for índice, gol in enumerate(time[cod]['gols']):
        print(f"\tNo {índice+1}º jogo fez {gol} gols.")
    print('--'*30)
print("VOLTE SEMPRE!")
