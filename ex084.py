dados = list()
pessoa = list()
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Peso [kg]: ')))
    pessoa.append(dados[:])
    dados.clear()
    resp = input('Deseja continuar? [S/N]').strip().upper()[0]
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break

print('=-'*25)
print(f'Ao todo voce cadastrou {len(pessoa)} pessoas.')
for i in range(0, len(pessoa)-1):
    if i == 0:
        maiorPeso = pessoa[i][1]
        menorPeso = pessoa[i][1]
    if pessoa[i][1] > maiorPeso:
        maiorPeso = pessoa[i][1]
    if pessoa[i][1] < menorPeso:
        menorPeso = pessoa[i][1]

print(f'Maior peso: {maiorPeso}', end='  ')
for nome, peso in pessoa:
    if peso == maiorPeso:
        print(f'{nome} ', end=' ')
print(f'\nMenor peso: {menorPeso}', end=' ')
for nome, peso in pessoa:
    if peso == menorPeso:
        print(f'{nome} ', end=' ')
