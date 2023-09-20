valores = []

cont = 0
while True:
    valores.append(int(input('Digite um valor: ')))
    cont += 1
    while True:
        resp = input('Deseja continuar? [S/N] ').upper()
        if resp in 'SN':
            break
    if resp == 'N':
        break

print('--'*25)
print(f'Foram digitados {cont} valores')
valores.reverse()
print(f'Valores digitados em ordem descrescente foram {valores}')
print(f'O valor 5 foi digitado? {5 in valores}')
