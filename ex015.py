dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
tot = (dias * 60) + (km * 0.15)

print(f'O total a pagar é R${round(tot, 2):.2f}')
