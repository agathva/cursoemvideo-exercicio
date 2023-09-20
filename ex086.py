matriz = list()
dados = list()
for l in range(0, 3):
    for c in range(0, 3):
        dados.append(int(input(f'Digite um valor para a posiçao [{l}][{c}]: ')))
    matriz.append(dados[:])
    dados.clear()

print('-='*25)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^8}]', end=' ')
    print()
