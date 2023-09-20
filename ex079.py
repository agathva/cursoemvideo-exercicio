valores = []

while True:
    x = int(input('Insira um valor: '))
    if x not in valores:
        valores.append(x)
        print('VALOR ADICIONADO COM SUCESSO!')
    else:
        print('VALOR DUPLICADO NÃO ADICIONADO!')
    while True:
        resp = input('Deseja continuar? [S/N] ').upper()
        if resp in 'SN':
            break
    if resp == 'N':
        break
    print('--'*25)
valores.sort()
print(f'Valores digitados {valores}')
