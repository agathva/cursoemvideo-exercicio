valores = []
pares = []
impares = []

while True:
    valores.append(int(input('Digite um valor: ')))
    while True:
        resp = input('Deseja continuar? [S/N] ').upper()
        if resp in 'SN':
            break
    if resp == 'N':
        break

for pos, num in enumerate(valores):
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'Todos os valores digitados {valores}')
print(f'Todos os valores pares digitados {pares}')
print(f'Todos os valores ímpares digitados {impares}')
