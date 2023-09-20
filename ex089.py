aluno = list()
dados = list()
while True:
    dados.append(input('Nome: '))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    aluno.append(dados[:])
    dados.clear()
    resp = input('Deseja continuar? [S/N]').strip().upper()[0]
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break

print('-='*25)
media = list()
for i in range(0, len(aluno)):
    media.append((aluno[i][1] + aluno[i][2]) / 2)
print('N°  Nome           Media')
for i in range(0, len(aluno)):
    print(f'{i}   {aluno[i][0]:<15} {round(media[i], 1)}')
print('-='*25)

while True:
    opçao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    print('--'*25)
    if opçao == 999:
        print('FIM')
        break
    else:
        print(f'Notas de {aluno[opçao][0]} sao {aluno[opçao][1]} e {aluno[opçao][2]}')
