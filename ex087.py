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

print('-='*25)
somaPar = somaC3 = maiorL2 = 0
for l in range(0, len(matriz)):
    for c in range(0, len(matriz)):
        if matriz[l][c] % 2 == 0:
            somaPar += matriz[l][c]
        if c == 2:
            somaC3 += matriz[l][c]
        if l == 1:
            if c == 0 or matriz[l][c] > maiorL2:
                maiorL2 = matriz[l][c]
print(f'Soma de todos os valores pares digitados: {somaPar}')
print(f'Soma dos valores da terceira coluna: {somaC3}')
print(f'Maior valor da segunda linha: {maiorL2}')
