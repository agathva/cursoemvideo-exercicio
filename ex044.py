print('=='*20)
a = 'LOJAS DOS ANJOS'
print(f'{a:^40}')
print('=='*20)

preço = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO \n[ 1 ] à vista dinheiro/cheque \n[ 2 ] à vista no cartão \n[ 3 ] 2x no cartão \n[ 4 ] 3x ou mais no cartão')
opção = int(input('Sua opção '))
print('=='*20)

if opção == 1 or opção == 2 or opção == 3 or opção == 4:
    if opção == 1:
        total = preço - preço * 10 / 100
    elif opção == 2:
        total = preço - preço * 5 / 100
    elif opção == 3:
        total = preço
        parcela = preço / 2
        print(f'Sua compra será parcelada em 2x de R${round(parcela, 2):.2f}')
    else:
        total = preço + preço * 20 / 100
        totPracela = int(input('Quantas parcelas? '))
        parcela = total / totPracela
        print(f'Sua compra será parcelada em {totPracela}x de R${round(parcela, 2):.2f}')
    print(f'Sua compra de R${round(preço, 2):.2f} vai custar R${round(total, 2):.2f} no final.')
else:
    print('OPÇÃO INVÁLIDA de pagamente. Tente novamente!')
