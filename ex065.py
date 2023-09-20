maior = menor = qtdd = soma = 0
while True:
    num = int(input('Digite um número: '))
    soma += num
    qtdd += 1
    if num > maior:
        maior = num
    else:
        menor = num
    resposta = input('Deseja continuar? [S/N] ').strip().upper()
    while resposta != 'N' and resposta != 'S':
        resposta = input('Deseja continuar? [S/N] ').strip().upper()
    print('--'*20)
    if resposta == 'N':
        break

media = soma / qtdd
print(f'A média de todos os {qtdd} valores digitados é {media}.')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}.')
