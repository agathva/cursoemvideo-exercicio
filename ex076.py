print('=='*23)
print(f'{"Listagem de preços":^43}')
print('=='*23)

produto = ('Borracha', '1.98', 'Corretivo', '3.31', 'Lapiseira', '2.16', 'Compasso', '9.62', 'Mochila', '135.98', 'Estojo', '14.79')
for pos in range(0, len(produto), 2):
    print(f'{produto[pos]:-<35} R${produto[pos+1]:>7}')
print('=='*23)