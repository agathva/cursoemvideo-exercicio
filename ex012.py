prod = float(input('Preço do produto: R$'))
aum = prod - prod * 5 / 100
print(f'O produto que custava R${round(prod, 2):.2f} na promoção vai custar R${round(aum , 2):.2f}')
