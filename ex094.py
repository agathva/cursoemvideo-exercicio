grupo = list()
pessoas = dict()
soma = 0

while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: ')).strip().title()
    while True:
        pessoas['sexo'] = str(input('sexo [M/F]: ')).strip().upper()[0]
        if pessoas['sexo'] in 'FM':
            break
        print('ERRO! Por favor, digite apenas M ou F!')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    grupo.append(pessoas.copy())
    while True:
        resp = str(input('Deseja continuar? (S/N) ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N')
    if resp in 'N':
        break

media = soma // len(grupo)
print('-='*25)
print(f'- O grupo tem {len(grupo)} pessoas')
print(f'- A média de idade é {media} anos')
print('- As mulheres cadastradas foram: ', end=' ')
for p in grupo:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print('\nLista das pessoas que estão acima da média: ')
for p in grupo:
    if p['idade'] >= media:
        print(f'\tNome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]};')
print('<<<ENCERRADO>>>')
