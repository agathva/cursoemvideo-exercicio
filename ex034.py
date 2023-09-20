sal = float(input('Salário: R$'))
if sal > 1250.00:
    aumento = sal + sal * 10 / 100
else:
    aumento = sal + sal * 15 / 100
print(f'Seu novo salário é de R${round(aumento, 2):.2f}')
