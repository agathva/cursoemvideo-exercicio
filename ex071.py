print('BANCO ALTO MAR')
print('=='*25)

saque = int(input('Valor a ser sacado: R$ '))

nota50 = saque // 50
saque = saque % 50
nota20 = saque // 20
saque = saque % 20
nota10 = saque // 10
saque = saque % 10
nota1 = saque // 1
saque = saque % 1

if nota50 > 0:
    print(f'Total de {nota50} cédulas de R$50,00.')
if nota20 > 0:
    print(f'Total de {nota20} cédulas de R$20,00.')
if nota10 > 0:
    print(f'Total de {nota10} cédulas de R$10,00.')
if nota1 > 0:
    print(f'Total de {nota1} cédulas de R$1,00.')
print('=='*25)
print('Volte sempre ao BANCO ALTO MAR! Tenha um bom dia!')
