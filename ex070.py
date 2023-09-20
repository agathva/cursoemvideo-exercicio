c = tot = qtdd1000 = 0

while True:
    nome = input('Nome do produto: ')
    preço = float(input('Preço: R$'))
    tot += preço
    c += 1
    if preço > 1000:
        qtdd1000 += 1
    if c == 1 or preço < barato:
        barato = preço
        baratoNome = nome
    print('--'*25)
    resp = input('Deseja continuar? [S/N] ').strip().upper()
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').strip().upper()
    if resp == 'N':
        break

print(f'Total gasto na compra: R${round(tot, 2):.2f}.')
print(f'{qtdd1000} produtos custam mais de mil reais.')
print(f'{baratoNome} foi o produto mais barato.')