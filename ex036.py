casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do pagador: R$'))
tempo = int(input('Quantos anos de financiamento: '))
prestação = round(casa/(tempo*12), 2)
print(f'Para pagar uma casa no valor de R${casa:.2f} em {tempo} anos a prestaçao será de R$ {prestação:.2f}')

if prestação > (30/100*salário):
    print('EMPRÉSTIMO NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')