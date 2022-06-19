print('Conversão de dólar em real')
print('=='*20)
real = float(input('Quanto você tem na carteira: R$'))

dolar = real / 4.80
euro = real / 5.12
libra = real / 6.00
iene = real / 0.037
print(f'R${round(real, 2):.2f} = €{round(euro, 2):.2f}')
print(f'R${round(real, 2):.2f} = £{round(libra, 2):.2f}')
print(f'R${round(real, 2):.2f} = ¥{round(iene, 2):.2f}')
print(f'R${round(real, 2):.2f} = US${round(dolar, 2):.2f}')
#print('R$%.2f = US$%.2f' %(round(real, 2), round(dolar, 2)))
#print('R${:.2f} = US${:.2f}'.format(round(real, 2), round(dolar, 2)))
