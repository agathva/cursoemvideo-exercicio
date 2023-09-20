valores = []
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))

maior = max(valores)
menor = min(valores)
posMaior = []
posMenor = []
for pos, num in enumerate(valores):
    if maior == num:
        posMaior.append(pos)
    if menor == num:
        posMenor.append(pos)

print('=='*25)
print(f'Valores digitados {valores}')
print(f'O maior valor digitado foi {maior} nas posições {posMaior}')
print(f'O menor valor digitado foi {menor} nas posições {posMenor}')

f'''
print(f'Valores digitados {valores}')
print(f'O maior valor digitado foi {max(maior)} nas posições {valores.index(max(valores))}')
print(f'O menor valor digitado foi {min(menor)} nas posições {posMenor.index(min(valores))}')
'''